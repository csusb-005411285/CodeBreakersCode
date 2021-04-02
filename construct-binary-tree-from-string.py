class Solution:
    def str2tree(self, s: str) -> TreeNode:
        nodes, index = self._str2_tree(s, 0)
        return nodes
    
    def _str2_tree(self, s, i):
        if i >= len(s):
            return None, i
        num, index = self.get_number(s, i)
        node = TreeNode(num)
        if index < len(s) and s[index] == '(':
            node.left, index = self._str2_tree(s, index + 1)
        if index < len(s) and s[index] == '(' and node.left:
            node.right, index = self._str2_tree(s, index + 1)
        if index < len(s) and s[index] == ')':
            return node, index + 1
        return node, index
    
    def get_number(self, s, i):
        is_neg = False
        num = 0
        if s[i] == '-':
            is_neg = True
            i += 1
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        return (-num, i) if is_neg else (num, i) 
