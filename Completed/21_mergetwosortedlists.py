# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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
                
        #recursive implementation
        #check if empty
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2