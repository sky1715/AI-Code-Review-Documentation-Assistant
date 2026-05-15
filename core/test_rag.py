# test_rag.py
from core.rag import get_context
from core.reviewer import review_code

print("=" * 50)
print("RAG CONTEXT TEST")
print("=" * 50)

# Test: what does ChromaDB find when we ask about file reading?
query = "def read_file"
context = get_context(query)
print(f"Query: '{query}'")
print(f"Retrieved context:\n{context}")

print("\n" + "=" * 50)
print("FULL REVIEW WITH RAG")
print("=" * 50)

# Test: review code that relates to the indexed codebase
test_code = """
def load_data(filepath):
    f = open(filepath)
    data = f.read()
    return data
"""
print(review_code(test_code))