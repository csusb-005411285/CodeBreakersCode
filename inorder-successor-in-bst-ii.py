class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        vert = None
        if not node.left and not node.right and not node.parent:
            return None
        if node.right:
            vert = node.right
            while vert and vert.left:
                vert = vert.left
            return vert
        while node and node.parent and node.parent.right is node:
            node = node.parent
        if node and node.parent and node.parent.left is node:
            return node.parent
        return None
