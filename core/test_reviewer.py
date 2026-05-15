# test_reviewer.py
from core.reviewer import review_code, generate_docstring, refactor_code

# A deliberately bad piece of code for testing
bad_code = """
def calculate(x, y, op):
    if op == 'add':
        return x + y
    if op == 'divide':
        return x / y
    if op == 'multiply':
        return x * y
"""

print("=" * 50)
print("BUG REVIEW")
print("=" * 50)
print(review_code(bad_code))

print("\n" + "=" * 50)
print("DOCSTRING GENERATOR")
print("=" * 50)
print(generate_docstring(bad_code))

print("\n" + "=" * 50)
print("REFACTOR")
print("=" * 50)
print(refactor_code(bad_code))