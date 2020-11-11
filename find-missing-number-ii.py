class Solution:
    def find_missing_number(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i]
            if j == len(nums):
                i += 1
            elif j == nums[j]:
                i += 1
            elif i != j:
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return -1 
