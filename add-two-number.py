class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        dummy = ListNode(float('inf'))
        curr = dummy
        carry = 0
        while p1 or p2:
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0
            sum_values = p1_val + p2_val + carry
            carry, num = divmod(sum_values, 10)
            new_node = ListNode(num)
            curr.next = new_node
            curr = curr.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        if carry:
            curr.next = ListNode(carry)
        return dummy.next
