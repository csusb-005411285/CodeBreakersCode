class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        # init a queue
        self.queue = deque()
        self.tree = root
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node and not node.left and not node.right:
                self.queue.append(node)
                continue
            if not node.left and node.right:
                self.queue.append(node)
            if node.left and not node.right:
                self.queue.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        node = None
        while self.queue:
            node = self.queue[0]
            if not node.left:
                node.left = new_node
                break
            else:
                node.right = new_node
                self.queue.popleft()
                break
        self.queue.append(new_node)
        return node.val
    
    def get_root(self) -> Optional[TreeNode]:
        # return the tree
        return self.tree
