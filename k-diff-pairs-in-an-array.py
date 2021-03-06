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
