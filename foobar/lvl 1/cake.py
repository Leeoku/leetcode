# The cake is not a lie!
# ======================

# Commander Lambda has had an incredibly successful week: she completed the first test run of her LAMBCHOP doomsday device, she captured six key members of the Bunny Rebellion, and she beat her personal high score in Tetris. 
# To celebrate, she's ordered cake for everyone - even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone, you'll get in big trouble. 

# The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. 
# Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

# To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise 
# (the decorations form a circle around the outer edge of the cake).

# Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases -- 
# Input:
# solution.solution("abcabcabcabc")
# Output:
#     4

# Input:
# solution.solution("abccbaabccba")
# Output:
#     2

# -- Java cases -- 
# Input:
# Solution.solution("abcabcabcabc")
# Output:
#     4

# Input:
# Solution.solution("abccbaabccba")
# Output:
#     2

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.



def solution(s):
    if len(s) <= 1:
        return 1

    #Check each length of string possible up to max length / 2 and pass to string validator. If all unique, return 1
    for i in range(1, len(s)//2 +1):
        #if true, that means this iteration is the longest string 
        if stringChecker(s, i):
            return int(len(s)/i)
    
    return 1

def stringChecker(s, length):
    #Find maximum number of substrings
    num_sub_strings = len(s)//length
    #Check each substring. If all pass, True
    for i in range (1, num_sub_strings):
        #Loop and check characters based on string length. J iterates through each character in the substring
        for j in range(0, length):
            #Check current character value
            current_letter = s[(i - 1) * length + j]
            #Check next character value
            next_letter = s[i * length + j]
            #Check if equal, if not return False
            if current_letter != next_letter:
                return False
    return True

print(solution('abccbaabccba'))
