# tc: o(n), sc: o(n)
def find_second_largest(root_node):
    stack = deque()
    stack.append(root_node)
    if root_node is None:
       raise 'Not a valid node' 
    
    if not root_node.left and not root_node.right:
       raise 'Not a valid node' 

    if root_node.right is None and root_node.left is not None:
        return root_node.left.value
    while stack:
        node = stack.pop()
        if node.right is not None and node.right.right is None and node.right.left is None:
            return node.value
        
        if node.right is None and node.left is not None:
            curr_node = node.left
            while curr_node.right:
                curr_node = curr_node.right
            return curr_node.value


        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    pass
