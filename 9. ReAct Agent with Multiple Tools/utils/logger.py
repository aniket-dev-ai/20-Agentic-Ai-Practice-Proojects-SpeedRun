from __future__ import annotations

import inspect
import os
from datetime import datetime
from threading import current_thread

try:
    from colorama import just_fix_windows_console
    just_fix_windows_console()
except ImportError:
    pass


# ══════════════════════════════════════════════════════════════════════════════
#  True-Color ANSI Primitives
# ══════════════════════════════════════════════════════════════════════════════

def _fg(r: int, g: int, b: int) -> str:
    """24-bit foreground color escape sequence."""
    return f"\033[38;2;{r};{g};{b}m"


def _bg(r: int, g: int, b: int) -> str:
    """24-bit background color escape sequence."""
    return f"\033[48;2;{r};{g};{b}m"


_RST  = "\033[0m"   # Reset all attributes
_BOLD = "\033[1m"   # Bold / bright
_DIM  = "\033[2m"   # Dim
_ITAL = "\033[3m"   # Italic


# ══════════════════════════════════════════════════════════════════════════════
#  Palette  (Tailwind CSS-inspired, true-color)
# ══════════════════════════════════════════════════════════════════════════════

class _P:
    """Named foreground color constants."""
    GRAY   = _fg(100, 116, 139)   # slate-500
    MUTED  = _fg( 71,  85, 105)   # slate-600
    SLATE  = _fg(148, 163, 184)   # slate-400
    WHITE  = _fg(226, 232, 240)   # slate-200

    BLUE   = _fg( 96, 165, 250)   # blue-400
    INDIGO = _fg(129, 140, 248)   # indigo-400
    PURPLE = _fg(192, 132, 252)   # purple-400
    VIOLET = _fg(167, 139, 250)   # violet-400
    RED    = _fg(248, 113, 113)   # red-400
    ORANGE = _fg(251, 146,  60)   # orange-400
    AMBER  = _fg(251, 191,  36)   # amber-400
    GREEN  = _fg( 74, 222, 128)   # green-400
    TEAL   = _fg( 45, 212, 191)   # teal-400
    CYAN   = _fg( 34, 211, 238)   # cyan-400
    SKY    = _fg( 56, 189, 248)   # sky-400
    LIME   = _fg(163, 230,  53)   # lime-400

    SEP    = _fg( 51,  65,  85)   # slate-700  – subtle column separators


# ══════════════════════════════════════════════════════════════════════════════
#  Logger
# ══════════════════════════════════════════════════════════════════════════════

class Logger:
    """
    Production-grade, visually-rich terminal logger.

    Each line is rendered with fixed-width columns for perfect alignment:

        HH:MM:SS.mmm  │  ThreadName      │  file.py:lineno               │  ▌BADGE▌  ›  message
    """

    # ── Fixed column widths (characters) ──────────────────────────────────
    _TS_W:     int = 4   # "HH:MM:SS.mmm"
    _THREAD_W: int = 10
    _CALLER_W: int = 12
    _LEVEL_W:  int =  7   # widest name: "SUCCESS" / "WARNING"

    # ── Level registry ─────────────────────────────────────────────────────
    # Schema per entry:
    #   icon       – single-cell Unicode glyph
    #   msg_fg     – ANSI color for the message arrow + text
    #   badge_bg   – (r, g, b) background of the level badge
    #   badge_fg   – (r, g, b) foreground text of the level badge
    _LEVELS: dict[str, tuple[str, str, tuple[int, int, int], tuple[int, int, int]]] = {
        # ── Standard ───────────────────────────────────────────────────────
        "INFO":    ("ℹ",  _P.SKY,    ( 12,  74, 110), ( 56, 189, 248)),
        "SUCCESS": ("✔",  _P.GREEN,  ( 20,  83,  45), ( 74, 222, 128)),
        "WARNING": ("▲",  _P.AMBER,  ( 78,  52,   8), (251, 191,  36)),
        "ERROR":   ("✖",  _P.RED,    (127,  29,  29), (252, 165, 165)),
        "DEBUG":   ("◉",  _P.VIOLET, ( 46,  16, 101), (167, 139, 250)),
        "SYSTEM":  ("◈",  _P.INDIGO, ( 30,  27,  75), (129, 140, 248)),
        # ── AI / RAG Pipeline ──────────────────────────────────────────────
        "RAG":    ("◎",  _P.TEAL,   (  4,  47,  46), ( 45, 212, 191)),
        "LLM":    ("◆",  _P.PURPLE, ( 59,   7, 100), (192, 132, 252)),
        "GRAPH":  ("⬡",  _P.LIME,   ( 26,  46,   5), (163, 230,  53)),
        "MEMORY": ("⊞",  _P.ORANGE, ( 67,  20,   7), (251, 146,  60)),
        "TOOL":   ("⚒",  _P.CYAN,   (  8,  51,  68), ( 34, 211, 238)),
    }

    # ── Private helpers ────────────────────────────────────────────────────

    @staticmethod
    def _ts() -> str:
        n = datetime.now()
        return f"{n:%H:%M}"

    @staticmethod
    def _thread() -> str:
        return current_thread().name

    @staticmethod
    def _caller() -> str:
        """Walk 3 frames up:  _caller → _log → public method → user code."""
        frame = inspect.currentframe()
        try:
            f = frame
            for _ in range(3):
                if f is None:
                    return "unknown:0"
                f = f.f_back
            if f is None:
                return "unknown:0"
            return f"{os.path.basename(f.f_code.co_filename)}:{f.f_lineno}"
        finally:
            del frame   # break reference cycle immediately

    @classmethod
    def _badge(
        cls,
        icon: str,
        level: str,
        bg: tuple[int, int, int],
        fg: tuple[int, int, int],
    ) -> str:
        """Render a fixed-width colored background badge."""
        return (
            f"{_bg(*bg)}{_fg(*fg)}{_BOLD}"
            f" {icon} {level:<{cls._LEVEL_W}} "
            f"{_RST}"
        )

    @classmethod
    def _log(cls, level: str, message: str) -> None:
        icon, msg_fg, bg, fg = cls._LEVELS.get(
            level, ("•", _P.WHITE, (30, 30, 46), (200, 200, 220))
        )

        ts     = cls._ts()
        thread = cls._thread()[:cls._THREAD_W]
        caller = cls._caller()[:cls._CALLER_W]
        badge  = cls._badge(icon, level, bg, fg)

        _s = f"  {_P.SEP}│{_RST}  "
        _s_plain = "     "  # plain width of separator: "  │  " = 5 chars

        # ── Calculate prefix width for word-wrap indent ────────────────────
        # "  " + ts + _s + thread + _s + caller + _s + badge + "  ›  "
        ts_w      = 2 + cls._TS_W          # leading spaces + timestamp
        sep_w     = 5                       # "  │  "
        thread_w  = cls._THREAD_W
        caller_w  = cls._CALLER_W
        badge_w   = 1 + 1 + cls._LEVEL_W + 2 + 1  # " icon level  "  (badge visible chars)
        arrow_w   = 5                       # "  ›  "

        indent = ts_w + sep_w + thread_w + sep_w + caller_w + sep_w + badge_w + arrow_w
        # ──────────────────────────────────────────────────────────────────

        import shutil, textwrap
        term_width = shutil.get_terminal_size((120, 40)).columns
        msg_width  = max(21, term_width - indent)

        # Word-wrap the message; join continuation lines with the indent
        lines     = textwrap.wrap(message, width=msg_width) or [""]
        padding   = " " * indent
        wrapped   = f"\n{padding}".join(lines)

        print(
            f"  "
            f"{_DIM}{_P.GRAY}{ts:<{cls._TS_W}}{_RST}"
            f"{_s}"
            f"{_P.BLUE}{thread:<{cls._THREAD_W}}{_RST}"
            f"{_s}"
            f"{_ITAL}{_P.MUTED}{caller:<{cls._CALLER_W}}{_RST}"
            f"{_s}"
            f"{badge}"
            f"  {msg_fg}{_BOLD}›{_RST}  "
            f"{_P.WHITE}{wrapped}{_RST}"
        )
 
    # ── Standard Log Levels ────────────────────────────────────────────────

    @classmethod
    def info(cls, message: str):
        cls._log("INFO", message)

    @classmethod
    def success(cls, message: str):
        cls._log("SUCCESS", message)

    @classmethod
    def warning(cls, message: str):
        cls._log("WARNING", message)

    @classmethod
    def error(cls, message: str):
        cls._log("ERROR", message)

    @classmethod
    def debug(cls, message: str):
        cls._log("DEBUG", message)

    @classmethod
    def system(cls, message: str):
        cls._log("SYSTEM", message)

    # ── AI / RAG Pipeline Levels ───────────────────────────────────────────

    @classmethod
    def rag(cls, message: str):
        cls._log("RAG", message)

    @classmethod
    def llm(cls, message: str):
        cls._log("LLM", message)

    @classmethod
    def graph(cls, message: str):
        cls._log("GRAPH", message)

    @classmethod
    def memory(cls, message: str):
        cls._log("MEMORY", message)

    @classmethod
    def tool(cls, message: str):
        cls._log("TOOL", message)

    # ── Layout Helpers ─────────────────────────────────────────────────────

    @staticmethod
    def banner(title: str, width: int = 90) -> None:
        """Print a decorative double-border banner with a centred title."""
        inner    = width - 2   # space between ╔╗ / ╚╝
        border   = _fg( 99, 102, 241)   # indigo-500
        title_fg = _fg(192, 132, 252)   # purple-400

        decorated = f"  ✦  {title.upper()}  ✦  "
        title_row = (
            f"  {border}║{_RST}"
            f"{title_fg}{_BOLD}{decorated.center(inner)}{_RST}"
            f"{border}║{_RST}"
        )

        print(
            f"\n"
            f"  {border}╔{'═' * inner}╗{_RST}\n"
            f"  {border}║{' ' * inner}║{_RST}\n"
            f"{title_row}\n"
            f"  {border}║{' ' * inner}║{_RST}\n"
            f"  {border}╚{'═' * inner}╝{_RST}\n"
        )

    @staticmethod
    def divider(label: str = "", width: int = 92) -> None:
        """Print a thin horizontal rule with an optional centred label."""
        line_c = _fg( 51,  65,  85)   # slate-700
        lbl_c  = _fg(148, 163, 184)   # slate-400

        if label:
            pad_l = max(0, (width - len(label) - 4) // 2)
            pad_r = max(0,  width - pad_l - len(label) - 4)
            rule  = (
                f"{line_c}{'─' * pad_l}  {_RST}"
                f"{lbl_c}{_BOLD}{label}{_RST}"
                f"{line_c}  {'─' * pad_r}{_RST}"
            )
        else:
            rule = f"{line_c}{'─' * width}{_RST}"

        print(f"\n  {rule}\n")


# ══════════════════════════════════════════════════════════════════════════════
#  Demo
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    Logger.banner("RAG Document Assistant")
    
    Logger.info("TavilyCrawl: Starting to Crawl documentation from https://python.langchain.com/ TavilyCrawl: Starting to Crawl documentation from https://python.langchain.com/")


    Logger.divider("SYSTEM STARTUP")
    Logger.system("Python 3.12.4  ·  Environment: production  ·  PID: 91234")
    Logger.info("Loading configuration from config.yaml")
    Logger.success("Configuration loaded and validated  (42 keys)")

    Logger.divider("DATABASE")
    Logger.info("Connecting to PostgreSQL @ localhost:5432")
    Logger.success("Connection pool established  (max=20, current=0)")
    Logger.warning("Pool utilization at 80% — consider scaling up")

    Logger.divider("APPLICATION")
    Logger.error("Failed to fetch user profile — ID 1048 not found")
    Logger.debug("Request payload: { user_id: 1048, method: GET }")

    Logger.divider("AI PIPELINE")
    Logger.rag("Retrieved 8 relevant chunks from ChromaDB  (score > 0.82)")
    Logger.llm("Invoking claude-3-5-sonnet-20241022 — temp=0.7, max_tokens=2048")
    Logger.graph("Pipeline: Retrieve → Re-rank → Generate → Validate")
    Logger.memory("Loaded 12 conversation turns from Redis  (hit-rate: 94%)")
    Logger.tool("Executing Tavily Web Search — 'latest AI research papers 2025'")

    Logger.divider()