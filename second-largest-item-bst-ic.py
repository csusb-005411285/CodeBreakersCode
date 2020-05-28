# tc: o(n), sc: o(n)
def find_second_largest(root_node):
    if not root_node.left and not root_node.right:
        raise Exception('Cannot find 2nd largest element')

    curr_node = root_node
    parent_node = root_node

    while curr_node and curr_node.right:
        parent_node = curr_node
        curr_node = curr_node.right

    if curr_node.left and not curr_node.right:
        return get_largest_element(curr_node.left)
    else:
        return parent_node.value

    raise Exception('Cannot find 2nd largest element')

def get_largest_element(node):
    curr_node = node

    while curr_node and curr_node.right:
        curr_node = curr_node.right

    return curr_node.value
