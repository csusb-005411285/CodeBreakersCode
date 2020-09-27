class Solution:
    def __init__(self):
        self.parents = []
    
    def find_parent(self, vert):
        if self.parents[vert] == vert:
            return vert
        
        return self.find_parent(self.parents[vert])
    
    def findCircleNum(self, M: [[int]]) -> int:
        m = M
        self.parents = [i for i in range(len(m))]
        clusters = 0

        for row in range(len(m)):
            for col in range(len(m[0])):

                if m[row][col] == 0:
                    continue

                parent_row = self.find_parent(row)
                parent_col = self.find_parent(col)

                if parent_col != parent_row:
                    self.parents[parent_col] = parent_row     

        for i in range(len(self.parents)):
            if self.parents[i] == i:
                clusters += 1
        
        return clusters
