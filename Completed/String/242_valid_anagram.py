# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

#Input string s and t, all lowercase alphabet
#output boolean
#edge case, empty string?, same length?

#Psuedo
# Make a dictionary add all letters in, then check letters t and remove
class Solution:
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

s = "anagram"
t= "nagaram"
Solution().isAnagram( s,t)

#Also use collection.counter
#  return collections.Counter(s) == collections.Counter(t)