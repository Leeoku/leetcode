class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class ListNode:
    def __init__ (self, x):
        self.val = x
        self.next = None

    #input = 1,2,3,4,5

    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 

    def reverseList(self,head):
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev

    def reverseListRecursive(self,head):

        #Condition if an empty linked list or reached the base case head
        if not head or not head.next:
            return head
        
        #Reverse the rest of the list
        node = self.reverseListRecursive(head.next)

        #Take the forward far pointer (next.next) and reverse it, then delete the forward pointer (next)
        head.next.next = head
        head.next = None

        #Fix Header Pointer
        return node


