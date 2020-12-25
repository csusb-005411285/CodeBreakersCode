class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
    def reverse_ll(self, head): 
        prev = None
        nxt = None
        curr = head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next 
        return prev
        
    def combine(self, first_half, second_half):
        first, second = first_half, second_half
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse_ll(slow)
        self.combine(head, rev)
