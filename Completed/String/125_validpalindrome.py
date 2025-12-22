# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:

# Input: "race a car"
# Output: false

# Using Strings
        # left, right = 0, len(s)-1
        # while left < right:
        #     if not s[left].isalnum():
        #         left +=1
        #     elif not s[right].isalnum():
        #         right -=1
        #     elif s[left].upper() == s[right].upper():
        #         left +=1
        #         right -=1
        #     else:
        #         return False
        # return True

# Using lists
clean_string = [letter for letter in s.upper() if letter.isalnum()]
left, right = 0, len(clean_string)-1
while left < right:
        if clean_string[left] !=  clean_string[right]:
        return False
        left +=1
        right -=1
return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [char.lower() for char in s if char.isalnum()]
        print(letters == letters[::-1])
        return letters == letters[::-1]
        
#         letters = [char.lower() for char in s if char.isalnum()]
#         return letters == list(reversed(letters))
s = 'A man, a plan, a canal: Panama'
Solution().isPalindrome(s)