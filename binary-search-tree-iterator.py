from collections import deque

class BSTIterator:

    def __init__(self, root: TreeNode):
        if not root:
            self.arr = []
        
        self.arr = deque() 
        self.bst_iterator_helper(root)

    def bst_iterator_helper(self, node): # 
        if not node:
            return
        
        if not node.left and not node.right:
            self.arr.append(node.val) 
            return

        if node.left:
            self.bst_iterator_helper(node.left) #

        self.arr.append(node.val) 

        if node.right:
            self.bst_iterator_helper(node.right) # 
        
        return

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.arr.popleft()
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.arr) > 0
        
