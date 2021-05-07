class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1 = self.inorder(root1)
        arr2 = self.inorder(root2)
        return self.merge(arr1, arr2)
    
    def inorder(self, root):
        stack = []
        res = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
    
    def merge(self, arr1, arr2):
        res = []
        p1 = 0
        p2 = 0
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] <= arr2[p2]:
                res.append(arr1[p1])
                p1 += 1
            else:
                res.append(arr2[p2])
                p2 += 1
        while p1 < len(arr1):
            res.append(arr1[p1])
            p1 += 1
        while p2 < len(arr2):
            res.append(arr2[p2])
            p2 += 1
        return res
