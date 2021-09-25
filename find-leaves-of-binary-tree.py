class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaf_nodes = []
        self.find_leaves(root, leaf_nodes)
        return leaf_nodes
    
    def find_leaves(self, node, leaf_nodes):
        if node and not node.left and not node.right:
            if not leaf_nodes:
                leaf_nodes.append([node.val])
            else:
                leaf_nodes[0] += [node.val]
            return 0
        left = right = 0
        if node.left:
            left = self.find_leaves(node.left, leaf_nodes)
        if node.right:
            right = self.find_leaves(node.right, leaf_nodes)
        height = max(left, right) + 1
        if height >= len(leaf_nodes):
            leaf_nodes.append([node.val])
        else:
            leaf_nodes[height] += [node.val]
        return height
