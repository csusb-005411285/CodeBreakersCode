class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_height = self.find_height(p)
        q_height = self.find_height(q)
        if p_height != q_height:
            if p_height > q_height:
                p = self.normalize_height(p, p_height - q_height)
            else:
                q = self.normalize_height(q, q_height - p_height)
        while p.parent and q.parent and p is not q:
            if p and p.parent is q:
                return q
            elif q and q.parent is p:
                return p
            else:
                p = p.parent
                q = q.parent
        return q
    
    def find_height(self, node):
        count = 0
        while node.parent:
            node = node.parent
            count += 1
        return count
    
    def normalize_height(self, node, height):
        while node and height:
            node = node.parent
            height -= 1
        return node
            
