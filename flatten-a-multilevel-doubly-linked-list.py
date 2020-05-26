class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        slow = head
        last_child = None
        self.flatten_helper(slow, last_child)
        curr_node = head
            
        return head
    
    def flatten_helper(self, slow, last_child):
        while slow and slow.next and not slow.child:
            slow = slow.next
        
        if slow.child is None and slow.next is None:
            return slow
        
        last_child = self.flatten_helper(slow.child, last_child)
        
        temp_next = slow.next
        slow.next = slow.child
        slow.child.prev = slow
        slow.child = None
        
        if last_child:
            last_child.next = temp_next
        
        if temp_next:
            temp_next.prev = last_child
        
        curr_child = None
        if last_child:
            curr_child = last_child.next
        
        while curr_child and curr_child.next:
            curr_child = curr_child.next
            
        return curr_child
        
