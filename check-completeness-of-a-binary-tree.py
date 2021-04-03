class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = deque()
        queue.append(root)
        found_null = False
        while queue:
            node = queue.popleft()
            if not node:
                found_null = True
            else:
                if found_null:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True
