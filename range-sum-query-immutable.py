class NumArray:

    def __init__(self, nums: List[int]):
        
        self.cache = nums
        for k in range(1, len(self.cache)):
            self.cache[k] += self.cache[k - 1]

    def sumRange(self, i: int, j: int) -> int:
        if len(self.cache) == 0:
            return 0
        prev_sum = self.cache[i - 1] if i >= 1 else 0
        curr_sum = self.cache[j]
        return curr_sum - prev_sum
