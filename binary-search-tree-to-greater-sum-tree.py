class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.helper(root, 0)
        return root
    
    def helper(self, node, num):
        if node is None:
            return num
        node.val += self.helper(node.right, num)
        return self.helper(node.left, node.val)
