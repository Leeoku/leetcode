# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:

# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [char.lower() for char in s if char.isalnum()]
        print(letters == letters[::-1])
        return letters == letters[::-1]
        
#         letters = [char.lower() for char in s if char.isalnum()]
#         return letters == list(reversed(letters))
s = 'A man, a plan, a canal: Panama'
Solution().isPalindrome(s)