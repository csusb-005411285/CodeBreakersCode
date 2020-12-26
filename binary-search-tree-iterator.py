from collections import deque

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder_list = []
        stack = deque()
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            self.inorder_list.append(node)
            root = node.right
        self.ptr = 0

    def next(self) -> int:
        node = None
        if self.hasNext():
            node = self.inorder_list[self.ptr].val
            self.ptr += 1
        return node

    def hasNext(self) -> bool:
        return self.ptr < len(self.inorder_list)

  
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
        
