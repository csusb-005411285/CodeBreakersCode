class Solution:
    def can_finish_eating_bananas(self, rate, piles, total_hours):
        hours = []
        for i, pile in enumerate(piles):
            hours.append(math.ceil((pile/rate)))
        return sum(hours) <= total_hours

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left)//2 
            if self.can_finish_eating_bananas(mid, piles, H):
                right = mid
            else:
                left = mid + 1
        return left
