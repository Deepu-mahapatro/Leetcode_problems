#DELETED NODE IN LINKED LIST

#DEFINITION FOR SINGLE-LINKED LIST
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def deleteNode(self,node):
        #COPY THE VALUE OF NEXT NODE
        node.val=node.next.val
        #SKIP THE NEXT NODE BY CHANGING THE POINTER
        node.next=node.next.next