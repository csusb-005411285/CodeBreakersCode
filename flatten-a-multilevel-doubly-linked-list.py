class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        self._flatten(head)
        return head
    
    def _flatten(self, node):
        curr = node
        next_level_last_node = None
        while curr and curr.next:
            if curr.child: break
            curr = curr.next
        # Pay attention to this step. 
        # Base case
        if curr.next is None and curr.child is None: return curr    
        if curr.child:
            next_level_last_node = self._flatten(curr.child)   
        curr_next = curr.next
        if next_level_last_node:
            next_level_last_node.next = curr_next
            if curr_next:
                curr_next.prev = next_level_last_node
        if curr.child:
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
        while curr.next:
            curr = curr.next
        return curr
