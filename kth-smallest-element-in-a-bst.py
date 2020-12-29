class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = deque()
        count = k
        while count:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            count -= 1
            root = node.right
        return node.val

# Recursive 
class Solution:
    def __init__(self):
        self.counter = 0
        self.kth_smallest = None

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.counter = k
        self.kth_smallest_helper(root)
        return self.kth_smallest
    
    def kth_smallest_helper(self, node):
        if self.counter == 0: return
        if not node: return
        self.kth_smallest_helper(node.left)
        self.counter -= 1
        if self.counter == 0:
            self.kth_smallest = node.val
            return
        self.kth_smallest_helper(node.right)
        return
