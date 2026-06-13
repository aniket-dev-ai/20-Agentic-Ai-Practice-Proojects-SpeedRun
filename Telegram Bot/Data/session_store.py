"""
Session Store
Each user gets an isolated session so conversations don't mix.

Structure:
sessions = {
    user_id: {
        "active": bool,
        "followup_count": int,
        "messages": [],
        "current_question": "",
        "session_complete": bool
    }
}
"""

from typing import TypedDict, List, Dict


class ConversationState(TypedDict):
    """LangGraph-ready state schema for a single user's conversation."""
    user_id: int
    messages: List[Dict[str, str]]
    followup_count: int
    current_question: str
    session_complete: bool


sessions = {}


def create_session(user_id: int):
    """Create a fresh session for a user (or reset if exists)."""
    sessions[user_id] = {
        "active": True,
        "followup_count": 0,
        "messages": [],
        "current_question": "",
        "session_complete": False
    }
    return sessions[user_id]


def get_session(user_id: int):
    """Get a user's session, creating one if it doesn't exist."""
    if user_id not in sessions:
        return create_session(user_id)
    return sessions[user_id]


def end_session(user_id: int):
    """Mark a session as inactive."""
    if user_id in sessions:
        sessions[user_id]["active"] = False


def reset_session(user_id: int):
    """Reset a user's session back to defaults."""
    return create_session(user_id)


def is_active(user_id: int) -> bool:
    return sessions.get(user_id, {}).get("active", False)


def add_message(user_id: int, role: str, content: str):
    """Append a message to the user's conversation history."""
    session = get_session(user_id)
    session["messages"].append({"role": role, "content": content})


def get_messages(user_id: int):
    return get_session(user_id)["messages"]


def increment_followup(user_id: int):
    session = get_session(user_id)
    session["followup_count"] += 1
    return session["followup_count"]


def set_current_question(user_id: int, question: str):
    session = get_session(user_id)
    session["current_question"] = question


def get_current_question(user_id: int) -> str:
    return get_session(user_id)["current_question"]


def set_session_complete(user_id: int, complete: bool = True):
    session = get_session(user_id)
    session["session_complete"] = complete


def is_session_complete(user_id: int) -> bool:
    return get_session(user_id).get("session_complete", False)


def get_conversation_state(user_id: int) -> ConversationState:
    """
    Build a LangGraph-ready state dict from the session store.
    Pass this directly as the input state to a LangGraph graph.
    """
    session = get_session(user_id)
    return ConversationState(
        user_id=user_id,
        messages=session["messages"],
        followup_count=session["followup_count"],
        current_question=session["current_question"],
        session_complete=session["session_complete"]
    )


def update_from_conversation_state(state: ConversationState):
    """
    Sync changes from a LangGraph state dict back into the session store.
    Call this after running the graph to persist updates.
    """
    user_id = state["user_id"]
    session = get_session(user_id)
    session["messages"] = state["messages"]
    session["followup_count"] = state["followup_count"]
    session["current_question"] = state["current_question"]
    session["session_complete"] = state["session_complete"]