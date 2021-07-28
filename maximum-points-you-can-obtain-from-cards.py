class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # define vars
        left = 0
        _min = float('inf')
        window_len = len(cardPoints) - k
        _sum = 0
        # initial checks
        if k == len(cardPoints):
            return sum(cardPoints)
        if k == 1:
            return max(cardPoints[0], cardPoints[-1])
        # sliding window
        for right, val in enumerate(cardPoints):
            _sum += val
            while right - left + 1 >= window_len and left <= right:
                if right - left + 1 == window_len:
                    _min = min(_min, _sum)
                _sum -= cardPoints[left]
                left += 1
        return sum(cardPoints) - _min
