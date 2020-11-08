class Solution:
    def __init__(self):
        self.combinations = []

    def combine(self, n: int, k: int) -> [[int]]:
        self.combine_helper(n, k, 1, [])
        return self.combinations
    
    def combine_helper(self, n, k, start, curr):
        if len(curr) == k:
            self.combinations.append(curr)
            return
        # Pay attention to n + 1, should be n + 1 and not n.
        for i in range(start, n + 1):
            # Pay attention to i + 1, do not confuse it with start + 1
            self.combine_helper(n, k, i + 1, curr + [i])
        return
