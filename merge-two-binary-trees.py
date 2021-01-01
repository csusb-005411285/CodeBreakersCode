# In-order traversal
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and not t2: return t1
        return self.merge_trees_helper(t1, t2)
    
    def merge_trees_helper(self, t1, t2):
        if not t1 and not t2:return 
        if not t1 and t2: return t2
        if t1 and not t2: return
        if t1 and t2: 
            t1.val = t1.val + t2.val
        left_node = self.merge_trees_helper(t1.left, t2.left)
        if not t1.left and left_node: t1.left = left_node
        right_node = self.merge_trees_helper(t1.right, t2.right)
        if not t1.right and right_node: t1.right = right_node
        return t1

# Post-order traversal
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.merge_trees_helper(t1, t2)

    def merge_trees_helper(self, t1, t2):
        if not t1 and not t2: return None
        if not t1 and t2: return t2
        if t1 and not t2: return t1
        left_child = self.merge_trees_helper(t1.left, t2.left)
        right_child = self.merge_trees_helper(t1.right, t2.right)
        if t1 and t2:
            t1.val += t2.val
        if not t1.left and left_child: t1.left = left_child
        if not t1.right and right_child: t1.right = right_child
        return t1
