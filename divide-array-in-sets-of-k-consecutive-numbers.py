class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        nums_counter = Counter(nums)
        for num in nums:
            if num in nums_counter:
                for i in range(num, num + k):
                    if i in nums_counter:
                        nums_counter[i] -= 1
                        if nums_counter[i] == 0:
                            del nums_counter[i]
                    else:
                        return False
        return True
