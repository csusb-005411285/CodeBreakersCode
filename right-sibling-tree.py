# n, 1
def rightSiblingTree(root):
    right_sibling_tree_helper(root, None, None)
    return root

def right_sibling_tree_helper(root, parent = None, is_left = False): # 
    if not root:
        return
    
    left, right = root.left, root.right
    right_sibling_tree_helper(left, root, True)

    if not parent:
        root.right = None
    elif is_left:
        root.right = parent.right
    elif not is_left:
        if not parent.right:
            root.right = None
        else:
            root.right = parent.right.left
    
    right_sibling_tree_helper(right, root, False)
