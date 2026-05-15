import streamlit as st

from core.reviewer import (
    review_code,
    generate_docstring,
    refactor_code
)

from core.language import (
    detect_language,
    LANGUAGE_MAP
)

st.set_page_config(
    page_title="AI Code Review Assistant",
    page_icon="🤖",
    layout="wide"
)

# ─────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────
st.title("🤖 AI Code Review & Documentation Assistant")

st.markdown("""
Analyze code using:
- AI-powered bug detection
- RAG-based code retrieval
- Automatic docstring generation
- Intelligent refactoring
""")

# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────
st.sidebar.title("⚙️ Settings")

task = st.sidebar.selectbox(
    "Choose Task",
    [
        "Code Review",
        "Generate Docstrings",
        "Refactor Code"
    ]
)

# ─────────────────────────────────────────────
# File Upload
# ─────────────────────────────────────────────
uploaded_file = st.file_uploader(
    "Upload Code File",
    type=[
        "py",
        "js",
        "ts",
        "java",
        "cpp",
        "c",
        "go"
    ]
)

code_input = ""

filename = "unknown.py"

language = "text"

# ─────────────────────────────────────────────
# Read Uploaded File
# ─────────────────────────────────────────────
if uploaded_file:

    code_input = uploaded_file.read().decode("utf-8")

    filename = uploaded_file.name

    detected_language = detect_language(filename)

    language = LANGUAGE_MAP.get(
        detected_language,
        "text"
    )

    st.success(f"Detected Language: {detected_language}")

    st.subheader("📄 Uploaded Code")

    st.code(
        code_input,
        language=language
    )

# ─────────────────────────────────────────────
# Manual Input
# ─────────────────────────────────────────────
else:

    st.subheader("📌 Paste Your Code")

    code_input = st.text_area(
        label="",
        height=350,
        placeholder="Paste your code here..."
    )

# ─────────────────────────────────────────────
# Run Button
# ─────────────────────────────────────────────
run_button = st.button("🚀 Run AI Analysis")

# ─────────────────────────────────────────────
# Processing
# ─────────────────────────────────────────────
if run_button:

    if not code_input.strip():

        st.error("Please provide some code.")

        st.stop()

    with st.spinner("Processing with AI..."):

        try:

            # ─────────────────────────────
            # Code Review
            # ─────────────────────────────
            if task == "Code Review":

                result = review_code(
                    code_input,
                    filename
                )

                st.success("Review completed!")

                st.subheader("🪲 Review Results")

                st.markdown(result)

            # ─────────────────────────────
            # Docstrings
            # ─────────────────────────────
            elif task == "Generate Docstrings":

                result = generate_docstring(
                    code_input
                )

                st.success("Docstrings generated!")

                st.subheader("📘 Updated Code")

                st.code(
                    result,
                    language=language
                )

            # ─────────────────────────────
            # Refactor
            # ─────────────────────────────
            elif task == "Refactor Code":

                result = refactor_code(
                    code_input
                )

                st.success("Refactoring completed!")

                st.subheader("✨ Refactored Code")

                st.code(
                    result,
                    language=language
                )

        except Exception as e:

            st.error("Something went wrong.")

            st.exception(e)

# ─────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────
st.markdown("---")

st.caption(
    "Built with Streamlit, RAG, ChromaDB, LangChain & LLMs"
)