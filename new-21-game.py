class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts: # 1.
            return 1
        dp = [1.0] + [0.0] * n
        _sum, prob = 1.0, 0.0
        for i in range(1, n + 1): # 2. 
            dp[i] += _sum / maxPts
            if i < k: # 4. 
                _sum += dp[i]
            else: 
                prob += dp[i]   
            if i - maxPts >= 0: # 3.
                _sum -= dp[i - maxPts]
        return prob

'''
1. Alice can only get points from 1 to k + maxPts
2. n + 1 to  include n
3. Shrink the window
4. k is the number of points and not the sum of the points
'''
