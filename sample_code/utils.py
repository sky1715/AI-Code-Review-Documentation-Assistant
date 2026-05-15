def read_file(path: str) -> str:
    """Read a file and return its contents as a string."""
    with open(path, 'r') as f:
        return f.read()

def chunk_text(text: str, chunk_size: int = 500) -> list:
    """Split text into chunks of a given size."""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def clean_code(code: str) -> str:
    """Remove blank lines and strip whitespace."""
    lines = [line for line in code.splitlines() if line.strip()]
    return '\n'.join(lines)