class Solution:
    def __init__(self):
        self.map = {0: [], 1: [TreeNode(0)]}
    
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        self.all_possible_fbt_helper(N)
        return self.map[N]

    def all_possible_fbt_helper(self, n):
        if n in self.map:
            return self.map[n]
        
        if n % 2 == 0:
            self.map[n] = []
            return self.map[n]    
        
        trees = []
        # loop through 1 to N + 1
        for i in range(n):   
            node = None
            # for each number create a new TreeNode
            prev_index = n - 1 - i
            left_childs = self.all_possible_fbt_helper(i)
            right_childs = self.all_possible_fbt_helper(prev_index)

            for l in left_childs:
                for r in right_childs:
                    node = TreeNode(0)
                    # get the left child from the memoization table
                    node.left = l 
                    # get the right child from the table
                    node.right = r
                    trees.append(node)
                    
        self.map[n] = trees         
        return self.map[n]
