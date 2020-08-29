class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.get_left_index(nums, target)
        right = self.get_right_index(nums, target)

        return [left, right] if left <= right else [-1, -1]

    def get_left_index(self, nums, target):
        l = 0 
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l)//2

            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return l

    def get_right_index(self, nums, target):
        l = 0 
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l)//2

            if nums[m] <=target:
                l = m + 1
            else:
                r = m - 1
        
        return r
