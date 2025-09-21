# Advanced String Checker
# Checks for palindrome, alphabetic characters, and balanced parentheses
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def is_alpha_only(s):
    return all(c.isalpha() for c in s if c.isalnum())

def balanced_parens(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

# Get input and run checks
s = input("Enter string: ")
print(f"Palindrome: {is_palindrome(s)}")
print(f"Alphabetic Only: {is_alpha_only(s)}")
print(f"Balanced Parentheses: {balanced_parens(s)}")