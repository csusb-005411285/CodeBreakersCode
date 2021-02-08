class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for i, num in enumerate(nums):
            if num != 0:
                self.pairs.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        p1 = 0
        p2 = 0
        while p1 < len(self.pairs) and p2 < len(vec.pairs):
            if self.pairs[p1][0] == vec.pairs[p2][0]:
                dot_product += self.pairs[p1][1] * vec.pairs[p2][1]
                p1 += 1
                p2 += 1
            elif self.pairs[p1][0] < vec.pairs[p2][0]:
                p1 += 1
            elif self.pairs[p1][0] > vec.pairs[p2][0]:
                p2 += 1
        return dot_product
