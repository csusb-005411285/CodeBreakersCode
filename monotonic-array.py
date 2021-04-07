class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        is_increasing = True
        is_decreasing = True
        for i, num in enumerate(A[1:], start = 1):
            if i - 1 >= 0 and A[i] < A[i - 1]:
                is_increasing = False
            if i - 1 >= 0 and A[i] > A[i - 1]:
                is_decreasing = False
        return is_increasing or is_decreasing
        
