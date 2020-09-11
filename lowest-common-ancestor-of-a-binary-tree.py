class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lowest_common_ancestor_helper(root, p, q)
    
    # 3 
    def lowest_common_ancestor_helper(self, node, p, q): # 3, 5, 1
        # if the node's value matches one of the two values
        if node.val == p.val or node.val == q.val:
            return node # 5
        
        # base case: if node is a leaf node
        if not node.left and not node.right: 
            return None
        
        left = None
        right = None
        # move left if node exists
        if node.left: # 5
            left = self.lowest_common_ancestor_helper(node.left, p, q) # 5
        # move right if node exists
        if node.right: # 
            right = self.lowest_common_ancestor_helper(node.right, p, q) # 
        # compare the return values and return
        
        # if the left and right are None 
        if not left and not right:
            return None
            # then return none

        # if left is None and right is not None; and the other way is valid too
        if not left and right:
            return right

        if not right and left:
            return left # 5

        return node # 
