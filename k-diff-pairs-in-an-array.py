# Two pointer
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        right = 0
        n = len(nums)
        nums.sort()
        while left < n and right < n:
            if abs(nums[right] - nums[left]) < k or left >= right: # 1.
                right += 1
            elif abs(nums[right] - nums[left]) == k:
                count += 1
                left += 1
                right += 1
                while left < n and nums[left - 1] == nums[left]:
                    left += 1
            else:
                left += 1
        return count

'''
1. Needed to pass the last test case, [1,1,1,2,2] k = 0
'''

# Concise solution
class Solution:
    def findPairs(self, nums: [int], k: int) -> int:
        nums_map = Counter(nums)
        result = []
        for i, v in nums_map.items():
            if k == 0 and v > 1:
                result.append(i)
            elif k > 0 and i + k in nums_map:
                result.append((i, i + k))
        return len(result)

# o(n), o(n)
class Solution:
    def findPairs(self, nums: [int], k: int) -> int:
        results = []
        num_map = Counter(nums)
         
        if k < 0:
            return 0
        
        if k == 0:
            count = 0
            for i, (key, value) in enumerate(num_map.items()):
                if value >= 2:
                    count += 1
            
            return count 
        
        for i in range(len(nums)):
            n = nums[i]

            if k + n in num_map:
                if [k + n, n] not in results:
                    results.append([k + n, n])
                
        return len(results)
