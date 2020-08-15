class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        
        left = 0
        right = len(nums) - 1 # 5 
        curr = 0
        n = nums

        while curr <= right: # 2, 4
            if n[curr] == 0: # 
                n[curr], n[left] = n[left], n[curr]
                left += 1 # 1
                curr += 1 # 2
            elif n[curr] == 1:
                curr += 1
            else:
                n[curr], n[right] = n[right], n[curr] 
                right -= 1 # 4
            
        return n
