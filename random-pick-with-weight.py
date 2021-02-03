class Solution:

    def __init__(self, w: List[int]):
        self.sum_weights = [0] * len(w)
        for i, num in enumerate(w):
            self.sum_weights[i] = num if i - 1 < 0 else num + self.sum_weights[i - 1]

    def pickIndex(self) -> int:
        random_num = random.randint(1, self.sum_weights[-1])
        left = 0
        right = len(self.sum_weights) - 1
        mid = 0
        while left <= right:
            mid = left + (right - left)//2
            if random_num == self.sum_weights[mid]:
                return mid
            if random_num < self.sum_weights[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
