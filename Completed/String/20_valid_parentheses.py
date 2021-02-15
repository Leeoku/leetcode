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

# Pseudo
# Create a dictionary of the valid brackets
# Check length of string, if odd, not possible to have valid brackets. If condition passed then it's even
# If even, do a for loop in each character
#     If match, add to stack
#     else if length of stack greater than 0 and the current character is equal to the previous char in dictionary, then remove it
#     Return False if condition doesn't match
# check if stack is empty 


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
            print("FALSE")
            return False
        
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif len(stack) > 0 and char == brackets[(stack[-1])]:
                stack.pop()
            else:
                print("FALSE LOOP")
                return False
        print(stack)
        return stack == []
input = "()[]{}"

Solution().isValid(input)
        

