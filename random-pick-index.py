class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        rand_index = 0
        for i, num in enumerate(self.nums):
            if num == target:
                rand_num = randint(0, count)
                if rand_num == count:
                    rand_index = i
                count += 1
        return rand_index

