class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        start = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(start)
        return self.merge(left, right)
    
    def merge(self, left, right):
        if not left or not right:
            return left or right
        l = left
        r = right
        dummy = ListNode(float('inf'))
        curr = dummy
        while l and r:
            if l.val <= r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
        curr.next = l or r
        return dummy.next
