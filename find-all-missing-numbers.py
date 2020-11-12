class Solution:
    def find_missing_numbers(self, nums):
        missingNumbers = []
        i = 0
        while i < len(nums):
            val = nums[i]
            if i + 1 != val and nums[val - 1] != val:
                nums[i], nums[val - 1] = nums[val - 1], nums[i] 
            else:
                i += 1 
        for k, v in enumerate(nums):
            if k + 1 != v:
                missingNumbers.append(k + 1) 
        return missingNumbers
