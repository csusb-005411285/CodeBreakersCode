class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        node_map = defaultdict(Node)
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            if curr.next not in node_map: 
                node_map[curr.next] = Node(curr.next.val) if curr.next else None
            if curr.random not in node_map: 
                node_map[curr.random] = Node(curr.random.val) if curr.random else None
            curr = curr.next
        curr = head
        while curr:
            node = node_map[curr]
            node.next = node_map[curr.next]
            node.random = node_map[curr.random]
            curr = curr.next
        return node_map[head]
    
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        curr_node = head 
        ll_map = defaultdict(Node)

        while curr_node:
            ll_map[curr_node] = Node(curr_node.val)
            curr_node = curr_node.next

        curr_node = head

        while curr_node:
            node = None
            node_next = None
            node_random = None

            if curr_node in ll_map:
                node = ll_map[curr_node]
            
            if curr_node.next in ll_map:
                node_next = ll_map[curr_node.next]
            
            if curr_node.random in ll_map:
                node_random = ll_map[curr_node.random]
            
            if node:
                node.next = node_next
                node.random = node_random
            
            curr_node = curr_node.next

        return ll_map[head]

