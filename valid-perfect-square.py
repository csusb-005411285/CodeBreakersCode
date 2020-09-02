class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, h = 1, num 

        while l <= h:
            mid = l + (h - l)//2

            if mid * mid == num:
                return True
            
            if mid * mid > num:
                h = mid - 1
            
            else:
                l = mid + 1

        return False
