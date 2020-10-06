class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0

        if not word1:
            return len(word2)
        
        if not word2:
            return len(word1)
        
        mat = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)] 

        for r in range(len(word2) + 1): 
            for c in range(len(word1) + 1):
                if r == 0:
                    mat[0][c] = c
                elif c == 0:
                    mat[r][0] = r
                else:
                    if word1[c - 1] == word2[r - 1]:
                        mat[r][c] = mat[r - 1][c - 1] 
                    else:
                        mat[r][c] = min(mat[r - 1][c], mat[r][c - 1], mat[r - 1][c - 1]) + 1

        return mat[-1][-1]
