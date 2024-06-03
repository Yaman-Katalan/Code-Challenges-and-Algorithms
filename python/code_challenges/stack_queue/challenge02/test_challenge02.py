import pytest
from challenge02 import is_valid_parentheses

def test_valid_cases():
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("()[]{}") == True
    assert is_valid_parentheses("[({})]") == True
    assert is_valid_parentheses("[(hello)()]") == True
    assert is_valid_parentheses("[{(())}]") == True

def test_invalid_cases():
    assert is_valid_parentheses("[({}]") == False
    assert is_valid_parentheses("[(])") == False
    assert is_valid_parentheses("{[}]") == False
    assert is_valid_parentheses("]") == False
    assert is_valid_parentheses("[") == False

def test_mixed_cases():
    assert is_valid_parentheses("(([[{{}}]]))") == True
    assert is_valid_parentheses("[[()]{}]") == True
    assert is_valid_parentheses("{[(])}") == False
    assert is_valid_parentheses("[()]{}{[()()]()}") == True
    assert is_valid_parentheses("[[[]") == False

if __name__ == "__main__":
    pytest.main()
