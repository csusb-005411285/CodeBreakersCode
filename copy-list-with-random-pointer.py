class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        p1 = head # 7
        p2 = None 
        p2_temp = None
        node_map = defaultdict(Node) 
        new_random_node = None
        new_next_node = None
        new_copy_node = None
        
        if not head:
            return None

        if not p1.next:
            if p1.random == p1:
                p2 = Node(p1.val, None, None)
                p2.random = p2
                return p2
            else:
                p2 = Node(p1.val, None, None)
                
            return p2
        
        curr_node = p1
        while curr_node: # 1
            node_map[curr_node] = Node(curr_node.val, None, None) # {7: N(7), 13: N(13), 11: N(11), 1: N(1)}
            curr_node = curr_node.next # n

        curr_node_2 = p1 
        while curr_node_2: # 7
            if curr_node_2.next in node_map: # 7
                node_map[curr_node_2].next = node_map[curr_node_2.next] # {7: N(7, N(13), None)}
                
            curr_node_2 = curr_node_2.next
        
        curr_node_rand = p1
        while curr_node_rand:
            if curr_node_rand.random in node_map:
                node_map[curr_node_rand].random = node_map[curr_node_rand.random]

            curr_node_rand = curr_node_rand.next

        return node_map[p1]
