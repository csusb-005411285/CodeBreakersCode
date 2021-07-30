class RangeModule:

    def __init__(self):
        self.map = defaultdict(int)

    def addRange(self, left: int, right: int) -> None:
        # 1. check for overlap
        start, end = left, right
        start_idx = []
        for prev_start, prev_end in self.map.items():
            if start <= prev_end and prev_start <= end:
                start = min(start, prev_start)
                end = max(end, prev_end)
                start_idx.append(prev_start)
        while start_idx:
            del self.map[start_idx.pop()]
        # 2. insert interval
        self.map[start] = end

    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.map.items(): # 10, 14
            if start <= left and right <= end: # 13 <= 14 and 10 <= 15
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        # 1. find overlapping ranges
        start, end = left, right
        start_idx = []
        for prev_start, prev_end in self.map.items():
            if start <= prev_end and prev_start <= end:
                start = min(start, prev_start)
                end = max(end, prev_end)
                start_idx.append(prev_start)
        # 2. delete interval
        while start_idx:
            del self.map[start_idx.pop()]
        # 3. add new intervals
        if start < left:
            self.map[start] = left
        if end > right:
            self.map[right] = end
            
# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
