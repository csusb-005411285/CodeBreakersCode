class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo = 1
        hi = max(piles)
        mid = 0
        while lo < hi:
            mid = lo + (hi - lo)//2
            if self.can_eat_all_bananas_at_current_rate(mid, H, piles):
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    def can_eat_all_bananas_at_current_rate(self, rate, total_hours, piles):
        return sum((pile - 1)//rate + 1 for pile in piles) <= total_hours
