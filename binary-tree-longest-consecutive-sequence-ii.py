# Easier to understand
class Solution:
    def __init__(self):
        self.max_path = 1 # 3.
    
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self._longest_consecutive(root)
        # check for no nodes
        return self.max_path
    
    def _longest_consecutive(self, node):
        # base case. check for leaf node
        if not node.left and not node.right:
            return [1, 1]
        # init vars
        left_incr = left_decr = right_incr = right_decr = 1 # 1.
        # move left
        if node.left:
            left_consec_incr, left_consec_decr = self._longest_consecutive(node.left)
        # move right
        if node.right:
            right_consec_incr, right_consec_decr = self._longest_consecutive(node.right)
        # if left child greater than 1
        if node.left and node.left.val + 1 == node.val:
            # add 1 to incr 
            left_incr += left_consec_incr
        # if left child is less than 1
        if node.left and node.left.val - 1 == node.val:
            # add 1 to decr
            left_decr += left_consec_decr
        # if right child is greater than 1
        if node.right and node.right.val + 1 == node.val:
            # add 1 to right incr
            right_incr += right_consec_incr 
        # if left child is less than 1
        if node.right and node.right.val - 1 == node.val:
            # add 1 to left child
            right_decr += right_consec_decr
        # combine left and right childs
        # left min + right max and right min and left max
        # store global variable
        max_child = max(left_incr, left_decr, right_incr, right_decr)
        max_through_root = max(left_incr + right_decr - 1, right_incr + left_decr - 1) # 2.
        self.max_path = max(self.max_path, max_child, max_through_root)
        return [max(left_incr, right_incr), max(left_decr, right_decr)]
'''
1.  We set it to 1 because even if a node is not part of increasing or decreasing, we stil return 1
2. We subtract 1 to prevent double counting
3. For a tree with one node, the max path is 1
'''

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
