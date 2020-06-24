def nodeDepths(root):
    queue = deque()
    queue.append([root, 0])
    sum_depths = 0

    while queue:
        node, depth = queue.popleft()

        sum_depths += depth

        if node.left: 
            queue.append([node.left, depth + 1])

        if node.right:
            queue.append([node.right, depth + 1])

    return sum_depths
