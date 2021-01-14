# Compact
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized_tree = []
        self._serialize(root, serialized_tree)
        return ','.join(serialized_tree)
    
    def _serialize(self, node, serialized_tree):
        if node is None:
            serialized_tree.append('x')
            return
        serialized_tree.append(str(node.val))
        self._serialize(node.left, serialized_tree)
        self._serialize(node.right, serialized_tree)
        return 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        node_list = split(',', data)
        return self._deserialize(node_list)
    
    def _deserialize(self, node_list):
        if not node_list:
            return None
        node_val = node_list.pop(0)
        if node_val == 'x':
            return None
        node = TreeNode(node_val)
        node.left = self._deserialize(node_list)
        node.right = self._deserialize(node_list)
        return node

class Codec:
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
        
        return ','.join([curr_node_val, left_child, right_child])
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(',')
        return self.deserialize_helper(lst)
    
    
    def deserialize_helper(self, data):
        node = data.pop(0) 
        
        if node == 'None':
            return None
       
        left_child = self.deserialize_helper(data)
        right_child = self.deserialize_helper(data)
        
        n = TreeNode(node)
        l = left_child
        r = right_child
        n.left = l
        n.right = r

        return n

