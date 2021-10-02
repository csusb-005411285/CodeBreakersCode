class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        cache = defaultdict(int)
        res = self._stone_game(stoneValue, 0, cache)
        if res > 0:
            return 'Alice'
        elif res < 0:
            return 'Bob'
        return 'Tie'
    
    def _stone_game(self, nums, i, cache):
        if i in cache:
            return cache[i]
        if i >= len(nums):
            return 0
        option2 = float('-inf')
        option3 = float('-inf')
        option1 = nums[i] - self._stone_game(nums, i + 1, cache)
        if i + 1 < len(nums):
            option2 = nums[i] + nums[i + 1] - self._stone_game(nums, i + 2, cache)
        if i + 2 < len(nums):
            option3 = nums[i] + nums[i + 1] + nums[i + 2] - self._stone_game(nums, i + 3, cache)
        cache[i] = max(option1, option2, option3)
        return cache[i]
    
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        cache = [float('-inf') for _ in range(len(stoneValue) + 1)]
        cache[-1] = 0
        for i in range(len(stoneValue) - 1, -1, -1):
            take = 0
            for j in range(3):
                if i + j < len(stoneValue):
                    take += stoneValue[i + j]
                    cache[i] = max(cache[i], take - cache[i + j + 1])
        if cache[0] < 0:
            return 'Bob'
        elif cache[0] > 0:
            return 'Alice'
        else:
            return 'Tie'
        
