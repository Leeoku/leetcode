# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

 

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# Example 4:

# Input: s = "([)]"
# Output: false

# Example 5:

# Input: s = "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        
        stack = []
        
        #condition that it's odd, no way there is valid paren.
        if len(s) % 2 != 0:
            return False
        
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif len(stack) > 0 and char == brackets.get(stack[-1]):
                stack.pop()
            return False
        return stack == []
input = "([}}])"

Solution().isValid(input)
        

