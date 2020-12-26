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
