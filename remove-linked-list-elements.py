class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(float('inf'))
        curr = head
        dummy.next = head
        prev = dummy
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    curr_next = curr.next
                    curr.next = None
                    curr = curr_next
                continue
            prev = curr
            curr = curr.next
        return dummy.next
