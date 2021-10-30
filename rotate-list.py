class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # init vars
        count = 1
        len_list = 0 
        # inital check
        curr = head 
        while curr: 
            curr = curr.next
            len_list += 1
        if k == 0 or not head: 
            return head
        k = k % len_list 
        if k == len_list or k == 0: 
            return head
        curr = head 
        # process
        while curr and count != len_list - k:
            curr = curr.next 
            count += 1 
        new_head = curr.next 
        ptr = curr
        while ptr.next: 
            ptr = ptr.next 
        ptr.next = head 
        curr.next = None
        # return
        return new_head 
