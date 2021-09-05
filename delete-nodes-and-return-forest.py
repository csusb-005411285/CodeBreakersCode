class Solution:
    def __init__(self):
        self.roots = []
    
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        self.del_nodes(root, to_delete_set, True) # 1.
        return self.roots
    
    def del_nodes(self, node, to_delete_set, parent_deleted):
        # base case
        # check for Null node
        if not node:
            return None
        # if node to be deleted in to_delete set
        if node.val in to_delete_set:
            # move left
            node.left = self.del_nodes(node.left, to_delete_set, True)
            # move right
            node.right = self.del_nodes(node.right, to_delete_set, True)
            return None
        # else
            # check if parent is deleted
        if parent_deleted:
        # if parent deleted
            # append node to result set
            self.roots.append(node)
            # if parent deleted or not deleted
                # build tree
        # move left
        node.left = self.del_nodes(node.left, to_delete_set, False)
        # move right
        node.right = self.del_nodes(node.right, to_delete_set, False)
        # return node
        return node
    
'''
1. For root node assume the parent does not exist or the parent is deleted.
'''
