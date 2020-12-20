class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = deque()
        q.append([(root, 1)])
        max_width = 1
        while q:
            nodes = q.popleft()
            neighbours = []
            for node, width  in nodes:
                if node.left:
                    neighbours.append((node.left, 2 * width))
                if node.right:
                    neighbours.append((node.right, (2 * width) + 1))
            if neighbours:
                max_width = max(max_width, neighbours[-1][1] - neighbours[0][1] + 1)
                q.append(neighbours)
        return max_width
