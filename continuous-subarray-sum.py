class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        num_map = defaultdict(list)
        cumulative_sums = []
        mod_val = 0
        num_map[0] = [-1] # Pay attention here.
        if len(nums) < 2:
            return False
        for i, num in enumerate(nums):
            val = num if i == 0 else cumulative_sums[-1] + num
            cumulative_sums.append(val)
        for key, val in enumerate(cumulative_sums):
            mod_val = val % k if k != 0 else val
            if mod_val in num_map:
                for j in num_map[mod_val]:
                    if key - j > 1:
                        return True
            else:
                num_map[mod_val].append(key)
        return False
