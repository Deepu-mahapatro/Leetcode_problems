#MIDDLE OF THE LINKED LIST

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #INITIALIZE TWO POINTERS
        #SLOW MOVE ONE STEP AT A TIME 
        #FAST MOVE TWO STEPS AT A TIME
        slow=head
        fast=head
        #CONTINUE UNTIL LAST NODE REACHES
        #WE CHECK BOTH BEACUASE FAST MOVE TWO STEPS 
        while fast and fast.next:
            #MOVE THE SLOW POINTER BY ONE SIDE
            slow=slow.next
            #MOVE FAST POINTER BY TWO NODES
            fast=fast.next.next
        #WHEN FAST REACHES THE END 
        #SLOW WILL BW THE POINTING TO THE MIDDLE NODE
        return slow
        