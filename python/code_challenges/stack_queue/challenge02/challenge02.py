# Write here the code challenge solution
def is_valid_parentheses(s):
    """
    Check if the input string has valid parentheses.
    
    :param s: The input string containing parentheses.
    :return: True if the parentheses are valid, False otherwise.
    """
    # Dictionary to keep track of matching pairs
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening brackets
    stack = []

    for char in s:
        if char in bracket_map:
            # Pop the top element if it's a match, otherwise use a dummy value
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            # Push the current character onto the stack if it's an opening bracket
            if char in bracket_map.values():
                stack.append(char)

    # The string is valid if the stack is empty
    return not stack

# Test cases
print(is_valid_parentheses("()"))         # Output: True
print(is_valid_parentheses("()[]{}"))     # Output: True
print(is_valid_parentheses("[({})]"))     # Output: True
print(is_valid_parentheses("[({}]"))      # Output: False
print(is_valid_parentheses("[(hello)()]"))  # Output: True
print(is_valid_parentheses("[{(())}]"))   # Output: True
