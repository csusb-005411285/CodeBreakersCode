def invertBinaryTree(tree):
    if not tree:
        return None

    invert_binary_tree_helper(tree)
    return tree

def invert_binary_tree_helper(root):
    if not root.left and not root.right:
        return root 

    left_child = None
    right_child = None
    
    if root.left:
        left_child = invert_binary_tree_helper(root.left)
    
    if root.right: 
        right_child = invert_binary_tree_helper(root.right) 

    root.left = right_child 
    root.right = left_child 

    return root 
