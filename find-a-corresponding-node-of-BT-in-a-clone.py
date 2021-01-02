# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        #In-Order Traversal of both trees 
        
        stack_original, stack_clone = deque([]), deque([])
        node_original, node_clone = original, cloned
        
        while stack_original or node_original:
            while node_original:
                stack_original.append(node_original)
                stack_clone.append(node_clone)
                node_original = node_original.left
                node_clone = node_clone.left
                
            cur_original = stack_original.pop()
            cur_clone = stack_clone.pop()
            
            if cur_original is target:
                return cur_clone
            
            node_original = cur_original.right
            node_clone = cur_clone.right
