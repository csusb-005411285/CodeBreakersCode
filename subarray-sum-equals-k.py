class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_sums = []
        subarray_sums = {0: 1}
        count = 0
        nums_sums.append(nums[0])
        
        for i in range(1, len(nums)):
            nums_sums.append(nums_sums[i - 1] + nums[i])

        for i in range(len(nums_sums)): # 4
            diff = nums_sums[i] - k  # 7 - 3 = 4

            if diff in subarray_sums: # 4
                val = subarray_sums[diff] # 1 
                count += val # 4

            if nums_sums[i] in subarray_sums: # 4 
                subarray_sums[nums_sums[i]] += 1
            else:
                subarray_sums[nums_sums[i]] = 1 # {0: 1, 1: 1, 3: 3, 4: 1}

        return count  
