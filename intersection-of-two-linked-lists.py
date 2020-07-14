# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
            
        p1 = headA
        p2 = headB

        while p1 is not p2:
            p1 = p1.next
            p2 = p2.next

            if not p1 and not p2:
                return None

            if not p1:
                p1 = headB

            if not p2:
                p2 = headA
        
        return p1
