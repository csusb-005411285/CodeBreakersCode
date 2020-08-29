    def isSymmetric(self, root: TreeNode) -> bool:
         return self.is_symmetric_helper(root, root)
    
    def is_symmetric_helper(self, t1, t2):
        if t1 is None and t2 is None:
            return True
            
        if t1 is None or t2 is None:
            return False 
        
        return t1.val == t2.val and self.is_symmetric_helper(t1.left, t2.right) and self.is_symmetric_helper(t1.right, t2.left)
