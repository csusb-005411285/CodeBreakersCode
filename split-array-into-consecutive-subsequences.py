class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        nums_freq_map = Counter(nums)
        existing_subsequence = defaultdict(int)
        for num in nums:
            if not nums_freq_map[num]:
                continue
            if existing_subsequence[num] > 0:
                existing_subsequence[num] -= 1
                existing_subsequence[num + 1] += 1
            elif nums_freq_map[num + 1] > 0 and nums_freq_map[num + 2] > 0:
                nums_freq_map[num + 1] -= 1
                nums_freq_map[num + 2] -= 1
                existing_subsequence[num + 3] += 1
            else:
                return False
            nums_freq_map[num] -= 1
        return True
