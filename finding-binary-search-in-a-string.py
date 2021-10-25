class Solution:
    def solve(self, s):
        return self.is_valid_subsequence(s, 'binarysearch', 0, 0, [])
    
    def is_valid_subsequence(self, s, subseq, i, j, indices):
        if j >= len(subseq):
            if len(indices) <= 2:
                return True
            diff = indices[1] - indices[0]
            for i in range(2, len(indices)):
                if indices[i] - indices[i - 1] != diff:
                    return False
            return True
        if i >= len(s):
            return False
        include = exclude = False
        if s[i] == subseq[j]:
            include = self.is_valid_subsequence(s, subseq, i + 1, j + 1, indices + [i])
        exclude = self.is_valid_subsequence(s, subseq, i + 1, j, indices)
        return include or exclude
