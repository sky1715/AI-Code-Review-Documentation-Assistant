EXTENSION_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".go": "Go"
}

LANGUAGE_MAP = {
    "Python": "python",
    "JavaScript": "javascript",
    "TypeScript": "typescript",
    "Java": "java",
    "C++": "cpp",
    "C": "c",
    "Go": "go"
}

def detect_language(filename: str) -> str:

    for ext, lang in EXTENSION_MAP.items():

        if filename.endswith(ext):
            return lang

    return "Unknown"