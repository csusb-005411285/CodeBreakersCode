def branchSums(root):
    if not root:
        return [0]

    if not root.left and not root.right:
        return [1]

    path = []
    branch_sum_helper([root, root.value], path)
    return path

def branch_sum_helper(root, path):
    node, sum_value = root 
    
    if not node.left and not node.right:
        path.append(sum_value) 
        return

    if node.left: 
        branch_sum_helper([node.left, node.left.value + sum_value], path) 
    
    if node.right: 
        branch_sum_helper([node.right, node.right.value + sum_value], path) 
    
    return
