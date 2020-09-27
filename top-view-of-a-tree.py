class Solution:
    def solve(self, root):
        if not root:
            return []

        node_dist = OrderedDict()
        queue = deque()
        queue.append((root, 0))

        while queue:
            node, dist = queue.popleft()
            
            if dist not in node_dist:
                node_dist[dist] = node

            if node.left:
                queue.append((node.left, dist - 1))
                
            if node.right:
                queue.append((node.right, dist + 1))

        return node_dist.values() 
