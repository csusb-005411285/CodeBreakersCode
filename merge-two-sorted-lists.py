class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = None
        ptr1 = l1
        ptr2 = l2
        if ptr1 is None and ptr2 is None: return None
        if ptr1 and ptr2 is None: return ptr1
        if ptr2 and ptr1 is None: return ptr2
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                ptr1_next = ptr1.next
                if curr is None:
                    curr = ptr1
                else:
                    curr.next = ptr1
                    curr = curr.next
                ptr1 = ptr1_next
            else:
                ptr2_next = ptr2.next
                if curr is None:
                    curr = ptr2
                else:
                    curr.next = ptr2
                    curr = curr.next
                ptr2 = ptr2_next
        if ptr2 is not None: curr.next = ptr2
        if ptr1 is not None: curr.next = ptr1
        return l1 if l1.val <= l2.val else l2
    
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
