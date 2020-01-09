# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA  is None and headB is None):
          return  None
        if (headA  is None and headB is not None):
          return  None
        if (headA  is not None and headB is None):
          return  None
        # initialize two pointers pA and pB
        pA = headA
        pB = headB
        # loop until the memory location of pA is not equal to memory location of pB
        while(pA is not pB):
          # if pA reaches the end then resume traversing headB
          if (pA is None):
            pA = headB
          else:
            pA = pA.next
          # if pB reaches the end then resume traversing headA
          if (pB is None):
            pB = headA
          else:
            pB = pB.next
        #return pA or pB
        return pA
