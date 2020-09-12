def minHeightBst(array):
    return min_height_bst_helper(array)

def min_height_bst_helper(a):
    # base case is when the array has one element or no elements
    if len(a) == 0:
        return None
    
    if len(a) == 1:
        return BST(a[0])

    # reduction step:
    # calculate the mid of the array using binary search
    mid = len(a)//2 
    # recursively call the function using the left and right half of the array
    l = min_height_bst_helper(a[:mid]) 
    r = min_height_bst_helper(a[mid + 1:]) 
    # recurrence relation would be creating a node and adding the left and right children
    node = BST(a[mid])
    node.left = l
    node.right = r

    # return the newly created node
    return node 
