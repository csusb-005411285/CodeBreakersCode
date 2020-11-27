class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.count == 0 or num > self.large[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, -num)
        if len(self.small) > len(self.large) and len(self.small) - len(self.large) >= 2:
            top = heappop(self.small)
            heappush(self.large, -top)
        elif len(self.large) > len(self.small) and len(self.large) - len(self.small) >= 2:
            top = heappop(self.large)
            heappush(self.small, -top)
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0: 
            return ((-self.small[0]) + self.large[0])/2
        else:
            return -self.small[0] if len(self.small) > len(self.large) else self.large[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
