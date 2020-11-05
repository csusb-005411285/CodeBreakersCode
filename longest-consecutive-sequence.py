class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        # init a dict to store the nums
        hmap = defaultdict()
        hmap = {nums[i] for i in range(len(nums))}
        # use a list to store if a number has been previously visited
        visited = set() 
        max_len = float('-inf')
        for num in nums: 
            longest_consecutive = 1
            if num in visited:
                continue
            visited.add(num) 
            while num + 1 in hmap: 
                longest_consecutive += 1 
                visited.add(num + 1)
                num += 1
            max_len = max(max_len, longest_consecutive) 
        return max_len 
