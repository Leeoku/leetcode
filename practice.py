print("Hello")


'''
Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.
'''


I 
-Sorted 
- DS LL
-ALL INTS , Yes
- 0 < n < 1000


O 
One Sorted LL
Combining LL 1 + LL2 

E  

Edge 1: what if LL is empty?
1-2-3
-



A

Temp allowed

     x
1  2-4


x   
1-3-4

#use a temporary node and use that as a reference head
  #temp head
  
  #ListNode(-1)
  #l3.next -> ListNode
  #l3.val -> int
  
  x 
1-4-5-6-null
      x
2-3-4-null

    x
-1 - 1 - 2 - 3 - 4 


class Solution:
    def mergeTwoLists(self, l1, l2):
      #check if empty
      if not l1 or not l2:
        return l1 or l2
      head = l3 = ListNode(-1)
      while l1 and l2:
        if l1.val < l2.val:
          l3.next = l1
          l1 = l1.next
        elif l2.val <= l1.val:
          l3.next = l2
          l2 = l2.next  
        l3 = l3.next
      if l1 or l2:
        l3.next = l1 or l2
      l3.next = l1 or l2 
      return head.next
          
          
              # l3 = pointer = ListNode(0)
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         pointer.next = l1
        #         l1 = l1.next
        #     else:
        #         pointer.next = l2
        #         l2 = l2.next
        #     pointer = pointer.next
        # #if one of the linked list ends, append the other one
        # pointer.next = l1 or l2
        # return l3.next

The interview would consist of a whiteboard technical QA, a coding challenge on a computer we will provide, as well as an opportunity for you to see the work space and meet some of the team.
https://www.linkedin.com/jobs/view/2007158521/?refId=4c8a06b8-81f7-4708-9fd1-9bcf9db2672c

# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

BFS 4729631
DFS :
Preorder
Stack:4 7
Values:4

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

  000
  101
  011

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''

I
Matrix List of INTS
Values are only 1,0

O
Return an integer


E

A
I = COLUMNS
J = ROWS
002200
002000
100001
= 1



000000
000000
000001
=3

class Solution(object):
    def numIslands(self, grid):
        islands = 0
        for i in range(len(grid)):  
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    self.part_of_island(i,j,grid)
        return islands

    def part_of_island(self, i, j,grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            return
        
        grid[i][j] = '2'
                
        self.part_of_island(i,j+1,grid)
        self.part_of_island(i,j-1,grid)
        self.part_of_island(i+1,j,grid)
        self.part_of_island(i-1,j,grid) 
