class Solution:
    def __init__(self):
        self.largest_diff = 0

    def solve(self, root):
        self._solve(root, [])
        return self.largest_diff

    def _solve(self, node, path):
        if not node:
            return
        if node and not node.left and not node.right:
            path.append(node.val)
            max_val = max(path)
            min_val = min(path)
            self.largest_diff = max(self.largest_diff, abs(max_val - min_val))
            return
        self._solve(node.left, path + [node.val])
        self._solve(node.right, path + [node.val])
        return
