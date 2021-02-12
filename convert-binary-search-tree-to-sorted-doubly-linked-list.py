class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        head, tail = self._tree_to_doubly_linked_list(root)
        head.left = tail
        tail.right = head
        return head
    
    def _tree_to_doubly_linked_list(self, node):
        if node and not node.left and not node.right:
            return (node, node)
        head, tail = node, node
        if node.left:
            lhead, ltail = self._tree_to_doubly_linked_list(node.left)
            ltail.right = node
            node.left = ltail
            head = lhead
        if node.right:
            rhead, rtail = self._tree_to_doubly_linked_list(node.right)
            node.right = rhead
            rhead.left = node
            tail = rtail
        return (head, tail)
