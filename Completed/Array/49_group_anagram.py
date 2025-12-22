from collections import defaultdict

# - create a dictionary
# - iterate over each word
# - for each word, sort it to make it a unique key
# - put the word into the dict key
# - return the dict values as a list

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sorted = sorted(s)
            result[sorted].append(s)
        return list(result.values())
    

strs = ["act","pots","tops","cat","stop","hat"]
Solution().groupAnagrams(strs)