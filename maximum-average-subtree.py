class Solution:
    def __init__(self):
        self.max_avg = 0
        
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self._max_avg_subtree(root, 0)
        return self.max_avg
    
    def _max_avg_subtree(self, node, num_nodes):
        if node and not node.left and not node.right:
            self.max_avg = max(self.max_avg, node.val)
            return (node.val, 1)
        left_child_val = 0
        right_child_val = 0
        num_left_nodes = 0
        num_right_nodes = 0
        if node.left:
            left_child_val, num_left_nodes = self._max_avg_subtree(node.left, num_nodes)
        if node.right:
            right_child_val, num_right_nodes = self._max_avg_subtree(node.right, num_nodes)
        sum_nodes = left_child_val + right_child_val + node.val
        num_of_nodes = num_left_nodes + num_right_nodes + 1
        avg = sum_nodes/num_of_nodes
        self.max_avg = max(self.max_avg, avg)
        return (sum_nodes, num_of_nodes)
