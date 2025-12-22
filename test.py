# Reverse string

s.reverse()
        # while loop implementation
        # left = 0
        # right = len(s)-1
        
        # while left<right:
        #     s[left], s[right] = s[right], s[left]
        #     left +=1
        #     right -=1

# Fizzbuzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #psuedo
        #for every item, check the modulo and return the output
        #To make it more efficient, use modulo with booleans
        return(["Fizz"*(not i%3)+"Buzz"*(not i%5) or str(i) for i in range(1,n+1)])

# Anagram
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        # add all of s to dict
        for i in s:
            if i not in seen:
                seen[i] = 0
            seen[i] +=1
        # compare letters in t and subtract
        for j in t:
            if j not in seen:
                return False
            else:
                seen[j] -= 1
        #check to see if all 0
        return (not any(seen.values()))

#palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [char.lower() for char in s if char.isalnum()]
        print(letters == letters[::-1])
        return letters == letters[::-1]