class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        nums = arr
        left = 0
        right = len(nums) - 1
        min_index = len(nums) - 1 
        min_num = float('inf')
        res = []

        for i in range(len(nums)):
            # find the minimum number
            if abs(min_num - x) > abs(nums[i] - x):
                min_num = nums[i]
                # store the minimum index
                min_index = i
            
        # get the index to the left of the min. number 
        left_index = min_index - 1 
        # get the index to the right of the min. number 
        right_index = min_index + 1 
        res.append(nums[min_index])
        k -= 1

        # 1 2
        while k >= 1:
            if left_index >= 0 and right_index < len(nums):
                if x - nums[left_index] <= nums[right_index] - x:
                    res.insert(0, nums[left_index])
                    left_index -= 1
                else:
                    res.append(nums[right_index])
                    right_index += 1
            else:
                if left_index < 0 and right_index < len(nums):
                    res.append(nums[right_index])
                    right_index += 1
                elif left_index >= 0 and right_index >= len(nums):
                    res.insert(0, nums[left_index])
                    left_index -= 1
                
            k -= 1
        
        return res
