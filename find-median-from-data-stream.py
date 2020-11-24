class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller_heap = []
        self.larger_heap = []
        self.count = 0
        

    def addNum(self, num: int) -> None:
        if self.count % 2 == 0:
            if self.count == 0:
                heappush(self.larger_heap, num)
            elif num < -self.smaller_heap[0]:
                top_ele = heappop(self.smaller_heap)
                heappush(self.larger_heap, -top_ele)
                heappush(self.smaller_heap, -num)
            else:
                heappush(self.larger_heap, num)
        else:
            if num > self.larger_heap[0]:
                top_ele = heappop(self.larger_heap)
                heappush(self.smaller_heap, -top_ele)
                heappush(self.larger_heap, num)
            else:
                heappush(self.smaller_heap, -num)
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (self.larger_heap[0] - self.smaller_heap[0])/2
        else:
            return self.larger_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
