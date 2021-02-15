# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its level order traversal as:

# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        final = []
        queue = deque()

        #check for root node
        if root:
            queue.append(root)
        while queue:
            level = []
            size = len(queue)

            for i in range(size):
            #take left most value and add the values into the level
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            final.append(level)
        return final