# https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31495/Should-be-6-Liner/30226
class Solution:
    def generateTrees(self, n: int) -> [TreeNode]:
        return self.generate_trees_helper(1, n)
    
    def generate_trees_helper(self, left_leaf, right_leaf):
        # if the value of left leaf is greater than the right leaf
        if left_leaf > right_leaf:
            # return None 
            return [None] 

        trees = []
        # loop from left leaf to right leaf,
        for i in range(left_leaf, right_leaf + 1):
            # for each node, calculate the left child and right child
            # left child is calculated from 1 to i - 1
            left_child = self.generate_trees_helper(left_leaf, i - 1)
            # right child is calculated from i + 1 to n
            right_child = self.generate_trees_helper(i + 1, right_leaf)

            # loop through the left child
            for lc in left_child:
                # loop through the right child
                for rc in right_child:
                    # create a new tree
                    root = TreeNode(i, None, None)
                    # attach the left child to the left pointer of root
                    root.left = left_child
                    # attach the right child to the right pointer of root
                    root.right = right_child
                    # append the tree to the list
                    trees += root

        # return the list
        return trees 
