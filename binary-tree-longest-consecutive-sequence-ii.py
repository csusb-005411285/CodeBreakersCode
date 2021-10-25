class Solution:
    def __init__(self):
        self.max_path = 0
    
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.get_longest_path(root)
        return self.max_path

    def get_longest_path(self, node):
        # base case, check for null node
        if not node: # 1.
            return [0, 0]
        # init variables
        # incr, decr
        incr = decr = 0
        # move left
        if node.left: # 
            left_incr, left_decr = self.get_longest_path(node.left) # [1, 1]
            # if current node + 1 == left child
            if node.val == node.left.val - 1:
                # set decr
                decr = max(decr, left_decr + 1) 
            # if current node - 1 == left child
            if node.val == node.left.val + 1:    
                # set incr
                incr = max(incr, left_incr + 1) # 2
        # move right
        if node.right:
            right_incr, right_decr = self.get_longest_path(node.right) # [1, 1]
            # if current node + 1 == right child
            if node.val == node.right.val - 1:    
                # set decr
                decr = max(decr, right_decr + 1)
            # if current node - 1 == right child
            if node.val == node.right.val + 1:    
                # set incr
                incr = max(incr, right_incr + 1)
        # set the max. value
        # the max. value would be a comparison between two paths and combination of both paths
        self.max_path = max(self.max_path, incr + decr - 1, incr, decr) # 3, 2, 0
        #return the max between two returned incr and decr
        return [incr, decr] #

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
