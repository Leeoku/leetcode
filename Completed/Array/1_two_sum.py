# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

#     2 <= nums.length <= 105
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.


#PSUEDO
# Create an initial empty dictionary. The dictionary will store {target-number: index}, target-number can also be the seen number complement
# Loop over the array of numbers
# Check to see if the number is in the dictionary
    # If yes, return the dictionary[number] to get the index
    # If no, add {target-number, index}

# nums = [2,7,11,15]
# target = 9
nums = [3,2,4]
target = 6
class Solution:
    def twoSum(self, nums, target: int) :
        seen = {}
        for index, num in enumerate(nums):
            print(index,num)
            if num in seen:
                print([seen[num], index])
                print(seen)
                return [seen[num], index]
            seen[target-num] = index
Solution().twoSum(nums, target) 