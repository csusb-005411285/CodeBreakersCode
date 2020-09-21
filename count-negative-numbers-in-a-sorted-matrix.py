class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        if len(grid) == 1 and len(grid[0]) == 0:
            return count

        for i in range(len(grid)): 
            count += self.count_negatives_helper(grid[i])
        
        return count

    def count_negatives_helper(self, a):
        l = 0
        r = len(a) - 1

        while l <= r:
            m = l + (r - l)//2

            if a[m] < 0:
                r = m - 1
            else:
                l = m + 1
        
        return len(a) - l
