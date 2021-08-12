# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # init vars
        left = head
        right = head
        dummy = ListNode(float('inf'))
        jump = dummy
        # check invalid inputs
        if k == 1 or not head.next:
            return head
        while True:
            count = 0
            # find k nodes to reverse
            while right and count < k:
                count += 1
                right = right.next
            if count == k:
                # reverse nodes
                prev = right # 2
                curr = left
                for i in range(k):
                    curr_next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = curr_next
                # rearrange pointers
                jump.next = prev # 1
                jump = left
                left = right
            # if no more nodes to reverse
            else:
                return dummy.next
        return head
