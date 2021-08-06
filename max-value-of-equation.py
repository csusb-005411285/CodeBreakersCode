class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # init vars
        que = deque()
        _max = float('-inf')
        # check for invalid input
        
        # perform operations
        for point in points:
            xj, yj = point
            while que and abs(que[0][1] - xj) > k:
                que.popleft()
            if que:
                _max = max(_max, que[0][0] + xj + yj)
            while que and que[-1][0] <= (yj - xj):
                que.pop()
            que.append((yj - xj, xj))
        return _max
