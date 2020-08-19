class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        # init a var left and right 
        left = 0
        right = 0
        node_val = 0

        if root.val >= L and root.val <= R:
            node_val = root.val

        # if L is less than or equal to the curr node:
        if L <= root.val:
            # move left
            left = self.rangeSumBST(root.left, L, R)
            
        # if R is greater than or equal to the curr node:
        if R >= root.val:
            # move right
            right = self.rangeSumBST(root.right, L, R)

        return node_val + left + right 
