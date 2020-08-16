class Solution:
    def sortArraySelectionSort(self, nums: [int]) -> [int]:
        for i in range(len(nums)):
            _min = float('inf')
            min_index = i

            for j in range(i + 1, len(nums)):
                if nums[j] <= nums[i]:
                    if nums[j] < _min:
                        _min = nums[j]
                        min_index = j

            nums[i], nums[min_index] = nums[min_index], nums[i]
        
        return nums

    def sortArray(self, nums: [int]) -> [int]:
        # 2 3 1 5
        for i in range(len(nums)): # 1
            for j in range(i, 0, -1): # 1
                if nums[j] < nums[j - 1]: # 3 < 3
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                else:
                    break
        
        return nums
