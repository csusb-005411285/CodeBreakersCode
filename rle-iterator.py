class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr = encoding
        self.index = 0 # 1

    def next(self, n: int) -> int:
        offset = n
        while offset > 0 and self.index < len(self.arr):
            if offset > self.arr[self.index]:
                offset -= self.arr[self.index]
                self.index += 2
            else:
                self.arr[self.index] -= offset
                return self.arr[self.index + 1]
        return -1

'''
1. self.index is the index of the encoded list and not the original list
'''
