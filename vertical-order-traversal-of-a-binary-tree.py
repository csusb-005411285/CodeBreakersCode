class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        node_list = []
        col_map = OrderedDict()
        queue.append((0, 0, root))
        while queue:
            last_element = queue.popleft()
            col, row, node = last_element
            node_list.append((col, row, node.val))
            if node.left:
                queue.append((col - 1, row + 1, node.left))
            if node.right:
                queue.append((col + 1, row + 1, node.right))
        node_list.sort(key = lambda x: (x[0], x[1], x[2]))
        for node in node_list:
            col, row, val = node
            if col not in col_map:
                col_map[col] = []
            col_map[col].append(val)
        return col_map.values()
