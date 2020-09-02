class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        thead = None
        curr = head
        prev = None
        
        # 1 -> 1
        while curr: # 1
            if curr.next and curr.val == curr.next.val: # 1 1 
                while curr and curr.next and curr.val == curr.next.val: # 1 n !!
                    curr = curr.next # 1
                
                tnext = curr.next # n

                if prev:
                    prev.next = tnext

                if curr:
                    curr.next = None # 1 -> n

                curr = tnext # n
            else:
                prev = curr # 1
                curr = curr.next # 2

                if not thead:
                    thead = prev
        
        return thead or prev or curr
