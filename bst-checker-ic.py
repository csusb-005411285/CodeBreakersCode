import unittest
from collections import deque

def is_binary_search_tree(root):
    # Determine if the tree is a valid binary search tree
    if not root:
        return False
    
    if not root.left and not root.right:
        return True

    # init  a deck
    stack = deque() #n 
    # the fist element of the deck should be the root along with +inf and -inf
    stack.append([root, float('-inf'), float('inf')])
    # loop through the binary tree
    while stack: #n
    # use iterative DFS
    # loop until stack is empty
        # pop the element
        element, min_val, max_val = stack.pop() 
        # if the value of element is less than min and greater than max 
        if element.value < min_val or element.value > max_val:
            # then return false
            return False
        
        # if the element has a left child
        if element.left: 
            # insert it to the deck, set the max to be value of element
            # and the min to be min value of the element
            stack.append([element.left, min_val, element.value])
            
        # if the element has a right child
        if element.right: 
            # insert it to the deck, set the min to be value of the element
            # and the max to be max value of the element
            stack.append([element.right, element.value, max_val])

    return True