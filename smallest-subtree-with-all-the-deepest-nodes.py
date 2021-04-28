class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self._subtree_with_deepest(root)[0]
    
    def _subtree_with_deepest(self, node):
        if not node:
            return (None, 0)
        left = self._subtree_with_deepest(node.left)
        right = self._subtree_with_deepest(node.right)
        if left[1] == right[1]:
            return (node, left[1] + 1)
        if left[1] > right[1]:
            return (left[0], left[1] + 1)
        else:
            return (right[0], right[1] + 1)
