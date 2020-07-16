class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        front = head
        back = head
        count = 1
        
        if not front.next:
            return front.next
        
        # 1 -> 2 k = 2
        while count <= n: # 2
            count += 1 # 3
            front = front.next # n

        if not front: # n
            back.val = back.next.val #  2
            back.next = back.next.next # 2 -> n
            
            return back

        while front.next: # 9
            front = front.next # 9
            back = back.next # 5

        back.next = back.next.next
        
        return head
