from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from html import escape
from langchain.tools import tool

 
def create_pdf(report):
    print("INSIDE TOOL")
 
    doc = SimpleDocTemplate(
        "report.pdf",
        pagesize=letter,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
    )

    # ---- Color palette ----
    PRIMARY = colors.HexColor("#2E3192")
    ACCENT = colors.HexColor("#1BC0C5")
    DARK = colors.HexColor("#1A1A2E")
    GRAY = colors.HexColor("#666666")
    LIGHT_BG = colors.HexColor("#F4F6FA")
    TOOL_BG = colors.HexColor("#EEF1FA")

    styles = getSampleStyleSheet()

    # ---- Custom styles ----
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=24,
        textColor=PRIMARY,
        alignment=TA_CENTER,
        spaceAfter=6,
        fontName="Helvetica-Bold",
    )

    meta_style = ParagraphStyle(
        "Meta",
        parent=styles["BodyText"],
        fontSize=9,
        textColor=GRAY,
        alignment=TA_CENTER,
        spaceAfter=2,
    )

    section_header = ParagraphStyle(
        "SectionHeader",
        parent=styles["Heading1"],
        fontSize=15,
        textColor=colors.white,
        backColor=PRIMARY,
        borderPadding=6,
        fontName="Helvetica-Bold",
        spaceAfter=10,
        spaceBefore=4,
    )

    tool_name_style = ParagraphStyle(
        "ToolName",
        parent=styles["Heading2"],
        fontSize=12,
        textColor=PRIMARY,
        fontName="Helvetica-Bold",
        spaceAfter=4,
    )

    label_style = ParagraphStyle(
        "Label",
        parent=styles["BodyText"],
        fontSize=9.5,
        textColor=DARK,
        fontName="Helvetica-Bold",
        spaceAfter=2,
    )

    body_style = ParagraphStyle(
        "BodyCustom",
        parent=styles["BodyText"],
        fontSize=10,
        textColor=DARK,
        leading=14,
        spaceAfter=6,
    )

    answer_style = ParagraphStyle(
        "Answer",
        parent=styles["BodyText"],
        fontSize=11,
        textColor=DARK,
        leading=16,
        backColor=LIGHT_BG,
        borderPadding=10,
    )

    content = []

    # ---- Title block ----
    content.append(Paragraph(escape(report["report_title"]), title_style))
    content.append(
        HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=8)
    )
    content.append(Paragraph(f"Generated At: {escape(str(report['generated_at']))}", meta_style))
    content.append(Spacer(1, 14))

    # ---- Query box ----
    query_table = Table(
        [[Paragraph(f"<b>Query:</b> {escape(report['user_query'])}", body_style)]],
        colWidths=[6.5 * inch],
    )
    query_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BG),
        ("BOX", (0, 0), (-1, -1), 0.5, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    content.append(query_table)
    content.append(Spacer(1, 18))

    # ---- Tools Used section ----
    content.append(Paragraph("🔧 Tools Used", section_header))
    content.append(Spacer(1, 6))

    for tool in report.get("tools_used", []):
        tool_block = []
        tool_block.append(Paragraph(escape(tool["tool_name"]), tool_name_style))
        tool_block.append(
            Paragraph(
                f"<b>Input:</b> {escape(str(tool['tool_input']))}",
                body_style,
            )
        )
        tool_block.append(
            Paragraph(
                f"<b>Output:</b> {escape(str(tool['tool_output'][:100]))}",
                body_style,
            )
        )

        tool_table = Table([[tool_block]], colWidths=[6.5 * inch])
        tool_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), TOOL_BG),
            ("LINEBEFORE", (0, 0), (-1, -1), 3, ACCENT),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]))
        content.append(tool_table)
        content.append(Spacer(1, 10))

    content.append(Spacer(1, 8))

    # ---- Final Answer ----
    content.append(Paragraph("✅ Final Answer", section_header))
    content.append(Spacer(1, 6))
    answer_table = Table(
        [[Paragraph(escape(report["final_answer"]), answer_style)]],
        colWidths=[6.5 * inch],
    )
    answer_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BG),
        ("BOX", (0, 0), (-1, -1), 0.75, PRIMARY),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    content.append(answer_table)
    content.append(Spacer(1, 18))

    # ---- Summary ----
    content.append(Paragraph("📝 Summary", section_header))
    content.append(Spacer(1, 6))
    content.append(Paragraph(escape(report["summary"]), body_style))

    doc.build(content)

    return "report.pdf"
