class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        self.flatten_helper(head)
        curr_node = head
        
        while curr_node:
            p(curr_node.val)
            curr_node = curr_node.next
            
        return head
    
    def flatten_helper(self, head):
        ptr = head

        while ptr.next and not ptr.child:
            ptr = ptr.next
        
        if not ptr.next and not ptr.child:
            return ptr
        
        last_child_node_next_level = self.flatten_helper(ptr.child)
        tmp_next_ptr = ptr.next
        
        if last_child_node_next_level: 
            last_child_node_next_level.next = tmp_next_ptr
            if tmp_next_ptr:
                tmp_next_ptr.prev = last_child_node_next_level
        
        ptr.next = ptr.child

        if ptr and ptr.child:
            ptr.child.prev = ptr
            ptr.child = None

        ptr = tmp_next_ptr
        last_child_node_curr_level = ptr

        while last_child_node_curr_level and last_child_node_curr_level.next:
            last_child_node_curr_level = last_child_node_curr_level.next
        
        return last_child_node_curr_level
