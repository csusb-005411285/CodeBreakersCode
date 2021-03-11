class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if s.val == t.val:
            if self._is_subtree(s, t):
                return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def _is_subtree(self, s, t):
        if not s and not t:
            return True
        if not t or not s:
            return False
        if s.val != t.val:
            return False
        return self._is_subtree(s.left, t.left) and self._is_subtree(s.right, t.right)

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.is_same(s, t):
            return True

        if not t and s:
            return True
        
        if not s and t:
            return False

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True

        if not s or not t:
            return False

        return (s.val == t.val) and self.is_same(s.left, t.left) and self.is_same(s.right, t.right) 
