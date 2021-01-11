class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build_tree_helper(preorder, inorder, 0, len(inorder) - 1)
    
    def build_tree_helper(self, preorder, inorder):
        if not preorder or not inorder: return None
        node_val = preorder.pop(0)
        new_node = TreeNode(node_val)
        index_in_inorder = inorder.index(node_val)
        new_node.left = self.build_tree_helper(preorder, inorder[:index_in_inorder])
        new_node.right = self.build_tree_helper(preorder, inorder[index_in_inorder + 1:])
        return new_node
    
    def build_tree_helper(self, preorder, inorder, start, end):
        if start > end: return None
        node_val = preorder.pop(0)
        new_node = TreeNode(node_val)
        index_in_inorder = inorder.index(node_val)
        new_node.left = self.build_tree_helper(preorder, inorder, start, index_in_inorder - 1)
        new_node.right = self.build_tree_helper(preorder, inorder, index_in_inorder + 1, end)
        return new_node
