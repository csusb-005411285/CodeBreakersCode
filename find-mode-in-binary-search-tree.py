class Solution:
    def __init__(self):
        self.ret = [[], 0]
        self.curr = None
        self.prev = None
        self.freq = 0

    def findMode(self, root: TreeNode) -> List[int]:
        self.find_mode_helper(root, False) 
        self.freq = 0
        self.find_mode_helper(root, True)
        
        return self.ret[0]

    def find_mode_helper(self, node, collect): # 
        """
        prev: [previous_value, count]. Need to survice the call stack
        """
        if not node:
            return

        self.find_mode_helper(node.left, collect) # 
        self.prev = self.curr
        self.curr = node

        if self.prev and self.prev.val == self.curr.val: # 
            self.freq += 1 # 2
        else:
            self.freq = 1 


        if not collect:
            self.ret[1] = max(self.ret[1], self.freq) 
        else:
            if self.freq == self.ret[1]:
                self.ret[0].append(node.val)

        self.find_mode_helper(node.right, collect) 
        
        return
