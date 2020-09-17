class Solution:
    def __init__(self):
        self.nodes = []
        self.prev = None
        self.curr = None
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.recover_tree_helper(root)
        
        if len(self.nodes) == 2:
            self.nodes[0][0].val, self.nodes[1][1].val = self.nodes[1][1].val, self.nodes[0][0].val
        else:
            self.nodes[0][0].val, self.nodes[0][1].val = self.nodes[0][1].val, self.nodes[0][0].val

        return root
    
    def recover_tree_helper(self, node):
        # base case
        # if null node
        if not node:
            # then return 
            return

        # reduction step
        # move left
        self.recover_tree_helper(node.left)
        # set the prev node and current node
        self.prev = self.curr 
        self.curr = node 
        # if prev node is not none and the value of the previous node is greater than the current node
        if self.prev and self.prev.val > self.curr.val:
            if not self.nodes:
                self.nodes = [(self.prev, self.curr)]
            # then add the two nodes to the list
            else:
                self.nodes.append((self.prev, self.curr))

        # move right
        self.recover_tree_helper(node.right)
        
        return
