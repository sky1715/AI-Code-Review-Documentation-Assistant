# core/reviewer.py
from fileinput import filename

from core.llm import ask_llm
from core.rag import get_context
from core.prompts import (
    DOCSTRING_SYSTEM,  DOCSTRING_USER,
    REFACTOR_SYSTEM,   REFACTOR_USER
)
from core.language import detect_language
from core.prompts import get_bug_review_system, get_bug_review_user

def review_code(code: str, filename: str) -> str:
    """Review code for bugs using RAG context from the codebase."""
    if not code.strip():
        return "Error: No code provided."

    language = detect_language(filename)
    bug_review_system = get_bug_review_system(language)
    bug_review_user = get_bug_review_user(code)

    # Retrieve relevant context from your indexed codebase
    context = get_context(code)

    # Build the user prompt — now includes codebase context
    user_prompt = bug_review_user
    if context:
        user_prompt = f"Relevant code context from the codebase:\n{context}\n\n{user_prompt}"

    return ask_llm(bug_review_system, user_prompt)


def generate_docstring(code: str) -> str:
    """Add docstrings to code."""
    if not code.strip():
        return "Error: No code provided."

    user_prompt = DOCSTRING_USER.format(code=code)
    return ask_llm(DOCSTRING_SYSTEM, user_prompt)


def refactor_code(code: str) -> str:
    """Refactor code to be more Pythonic."""
    if not code.strip():
        return "Error: No code provided."

    user_prompt = REFACTOR_USER.format(code=code)
    return ask_llm(REFACTOR_SYSTEM, user_prompt)