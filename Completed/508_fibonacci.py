# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.

# Given N, calculate F(N).

 

# Example 1:

# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:

# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:

# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

 

# Note:

# 0 ≤ N ≤ 30.

# Pseudo
# Check for exception where N = 0, return 0
# Create initial array for first two values of [0,1]
# Create a for loop from 2 to n+1
#     For each value, add the prev value and prev prev value

class Solution:
    def fib(self, N: int) -> int:
        #recursive
        # if N == 0:
        #     return 0
        # if N == 1 or N == 2:
        #     return 1
        # return self.fib(N-1) + self.fib(N-2)
        
        #Dynamic programming
        if N == 0:
            return 0
        nums = [0,1] 

        for i in range(2,N+1):
            nums.append(nums[i-1]+nums[i-2])
        return nums[N]
        