class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        curr_node = head # 1
        tmp_next = self.swapPairs(curr_node.next.next)
        curr_node.next.next = curr_node # 2 -> 1
        head = curr_node.next
        curr_node.next = tmp_next # 1 -> N
        
        return head
