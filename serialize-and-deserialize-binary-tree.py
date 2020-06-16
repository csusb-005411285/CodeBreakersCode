class Codec:
    # https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/396124/Python-very-easy-to-understand-recursive-preorder-with-comments
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized_path = ''
        serialized_path = self.serialize_helper(root)
        
        return serialized_path
     
    def serialize_helper(self, root):
        if not root:
            return 'x'
        
        curr_node_val = str(root.val)
        left_child = self.serialize_helper(root.left)
        right_child = self.serialize_helper(root.right)
        
        return [curr_node_val, left_child, right_child]
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] == 'x': return None
        
        node = TreeNode(data[0])
        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])
        
        return node
