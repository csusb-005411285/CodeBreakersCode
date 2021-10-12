class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        roots = []
        to_delete_set = set(to_delete)
        self.delete_nodes(root, to_delete_set, roots)
        if root.val not in to_delete_set:
            roots.append(root)
        return roots
        
    def delete_nodes(self, node, to_delete_set, roots):
        # base case
        # check for null
        if not node:
            return None
        # move left
        left = self.delete_nodes(node.left, to_delete_set, roots)
        # move right
        right = self.delete_nodes(node.right, to_delete_set, roots)
        # add the left child 
        node.left = left
        # add the right child
        node.right = right
        # if node.val in set
        if node.val in to_delete_set:    
            # add children to result set
            if node.left:
                roots.append(node.left)
            if node.right:
                roots.append(node.right)
            # return none
            return None
        # return node
        return node
