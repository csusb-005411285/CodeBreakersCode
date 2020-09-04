class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        a = A
        
        if len(a) < 3:
            return False

        total_sum = sum(a)
        one_third = total_sum//3
        left = 1
        right = len(a) - 2
        lsum = a[0]
        rsum = a[-1]

        while left <= right:
            if lsum !=  one_third:
                lsum += a[left]
                left += 1

            if rsum != one_third:
                rsum += a[right]
                right -= 1

            if left > right:
                return False

            if lsum == one_third == rsum:
                return True 

        return False
