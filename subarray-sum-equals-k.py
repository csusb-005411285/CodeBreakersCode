class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * len(nums)
        count = 0
        num_map = defaultdict(int)
        num_map[0] = 1
        for i, num in enumerate(nums):
            prefix_sum[i] = prefix_sum[i - 1] + num if i - 1 >= 0 else num
        for i, num in enumerate(prefix_sum):
            if num - k in num_map:
                count += num_map[num - k]
            num_map[num] += 1
        return count
    
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
