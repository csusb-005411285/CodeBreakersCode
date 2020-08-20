class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        local_min = 1 
        _max, local_max = float('-inf'), 1 
        
        for n in nums: 
            p1 = local_max * n
            p2 = local_min * n
            local_max = max(p1, p2, n) 
            local_min = min(p1, p2, n) 
            _max = max(_max, local_max)

        return _max
