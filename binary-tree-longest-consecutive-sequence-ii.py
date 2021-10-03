class Solution:
    def __init__(self):
        self.longest_path_len = 0
    
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # call helper method
        self.longest_consecutive(root, None)
        return self.longest_path_len
    
    def longest_consecutive(self, node, parent):
        # base case, null nod e
        if not node:
            return [0, 0]
        # init vars
        incr, decr, left_incr, left_decr, right_incr, right_decr = 0, 0, 0, 0, 0, 0
        # move left
        left_decr, left_incr = self.longest_consecutive(node.left, node)
        # move right
        right_decr, right_incr = self.longest_consecutive(node.right, node)
        # process
        # check if the next node is inceasing or decreasing, check for both children
        if parent:
            if node.val == parent.val + 1:
                incr = max(right_incr, left_incr) + 1
            if node.val == parent.val - 1:
                decr = max(left_decr, right_decr) + 1
        # compare the incr and decr count from children
        # set the global variable
        self.longest_path_len = max(self.longest_path_len, 1 + right_incr + left_decr, 1 + left_incr  + right_decr) # 1.
        # return the list of max values
        return [decr, incr]
    
'''
1. If a node has increasing and decreasing sequence, then it makes sense to add both the values. If it has either one of the two values, the above equation still holds true as the the remaining values are 0. 
'''
