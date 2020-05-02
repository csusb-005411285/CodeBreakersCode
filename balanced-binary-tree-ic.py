# tc: o(n), sc: o(n)
def is_balanced(tree_root):
    if tree_root is None:
        return False
    
    if not tree_root.left and not tree_root.right:
        return True
        
    diff = is_balanced_helper(tree_root, 0)
    if diff == -1:
        return False 
    else:
        return True 

# the recursive method returns the maximum depth tree not the depth of the node
def is_balanced_helper(node, depth = 0):
    if not node.left and not node.right:
        return depth 
    
    left_child_depth = depth 
    right_child_depth = depth 
    if node.left:
        left_child_depth = is_balanced_helper(node.left, depth + 1)
    if node.right:
        right_child_depth = is_balanced_helper(node.right, depth + 1)

    if left_child_depth > right_child_depth:
        diff = left_child_depth - right_child_depth
        if diff >= 2:
            return -1
        # return maximum depth
        return left_child_depth
    elif right_child_depth > left_child_depth:
        diff = right_child_depth - left_child_depth
        if diff >= 2:
            return -1
        # return maximum depth
        return right_child_depth
    else:
        # if the depths are same, return the depth
        return depth

# iterative implementation
# tc: o(n), sc: o(n)
def is_balanced(tree_root):
    stack = deque()
    stack.append([tree_root, 0])
    leaf_nodes = []
    min_depth = float('inf') 
    max_depth = float('-inf') 
    while stack:
        node, depth = stack.pop()
        if not node.left and not node.right:
            leaf_nodes.append([node, depth])
        if node.right:
            stack.append([node.right, depth + 1])
        if node.left:
            stack.append([node.left, depth + 1])

    for leaf_node in leaf_nodes:
        min_depth = min(min_depth, leaf_node[1]) 
        max_depth = max(max_depth, leaf_node[1])

    if max_depth - min_depth <= 1:
        return True 
    else:
        return False
