class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next: return None
        if not head.next: return head 
        if m == n: return head
        curr_node = head
        prev_mth_node, mth_node = self.get_nodes_till_m(head, m) 
        nth_node, next_nth_node = self.get_nodes_after_n(head, n) 
        if prev_mth_node: prev_mth_node.next = None
        if nth_node: nth_node.next = None
        reversed_list = self.reverse(mth_node)
        if prev_mth_node: prev_mth_node.next = reversed_list
        last_node = self.get_last_node(reversed_list)
        if last_node: last_node.next = next_nth_node
        return head if head is not mth_node else nth_node 

    def get_nodes_till_m(self, head, m):
        curr_node = head
        prev = None
        count = 1
        while count < m:
            prev = curr_node 
            curr_node = curr_node.next
            count += 1
        return (prev, curr_node) 
    
    def get_nodes_after_n(self, head, n):
        curr_node = head
        next_node = head
        count = 1
        while count < n:
            curr_node = curr_node.next
            if curr_node:
                next_node = curr_node.next
                count += 1
        return (curr_node, next_node) 

    def reverse(self, head):
        curr_node = head
        prev = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node
        return prev
    
    def get_last_node(self, head):
        curr_node = head
        while curr_node.next:
            curr_node = curr_node.next
        return curr_node
