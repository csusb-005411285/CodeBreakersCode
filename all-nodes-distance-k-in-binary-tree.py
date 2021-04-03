class Solution:
    def __init__(self):
        self.adj_list = defaultdict(list)
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        nodes_at_k = []
        queue = deque()
        visited = set()
        self.build_adj_list(root, None)
        queue.append((target, 0))
        while queue:
            node, dist = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            if dist == K:
                nodes_at_k.append(node.val)
            for neigh in self.adj_list[node]:
                queue.append((neigh, dist + 1))
        return nodes_at_k
    
    def build_adj_list(self, node, parent):
        if not node:
            return
        if node and parent:
            self.adj_list[node].append(parent)
            self.adj_list[parent].append(node)
        self.build_adj_list(node.left, node)
        self.build_adj_list(node.right, node)
        return
