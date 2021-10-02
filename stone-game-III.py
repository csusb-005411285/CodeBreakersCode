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
        
