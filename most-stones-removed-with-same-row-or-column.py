class Solution:
    def __init__(self):
        self.parents = []

    def find_parent(self, vert):
        if self.parents[vert] == vert:
            return vert
        
        return self.find_parent(self.parents[vert])
    
    def removeStones(self, stones: [[int]]) -> int:
        self.parents = [i for i in range(len(stones))]
        moves = 0

        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    pi = self.find_parent(i)
                    pj = self.find_parent(j)

                    if pi != pj:
                        self.parents[pj] = self.parents[pi]
                        moves += 1

        return moves 
