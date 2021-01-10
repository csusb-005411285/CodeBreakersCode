class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1, ptr2, dummy_head = l1, l2, ListNode(float('inf'))
        curr = dummy_head
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val <= ptr2.val:
                curr.next = ptr1
                curr = ptr1
                ptr1 = ptr1.next
            else:
                curr.next = ptr2
                curr = ptr2
                ptr2 = ptr2.next
        if ptr1 is not None:
            curr.next = ptr1
        if ptr2 is not None:
            curr.next = ptr2
        return dummy_head.next
    
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
