def searchForClosestNodeHelper(root, val, closestNode):
    if root is None:
        return closestNode

    if root.val == val:
        return root

    if closestNode is None or abs(root.val - val) < abs(closestNode.val - val):
        closestNode = root

    if val < root.val:
        return searchForClosestNodeHelper(root.left, val, closestNode)
    else:
        return searchForClosestNodeHelper(root.right, val, closestNode)

def searchForClosestNode(root, val):
    return searchForClosestNodeHelper(root, val, None)
