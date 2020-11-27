class ContinuousMedianHandler:
    def __init__(self):
		self.left_heap = []
        self.right_heap = []
        self.median = None
        self.count = 0
		
    def insert(self, number):
        if self.left_heap and number > -self.left_heap[0]:
            heappush(self.right_heap, number)
        else:
            heappush(self.left_heap, -number)
        if len(self.left_heap) > len(self.right_heap) and len(self.left_heap) - len(self.right_heap) >= 2:
            top_element = -heappop(self.left_heap)
            heappush(self.right_heap, top_element)
        elif len(self.right_heap) > len(self.left_heap) and len(self.right_heap) - len(self.left_heap) >= 2:
            top_element = -heappop(self.right_heap)
            heappush(self.left_heap, top_element)
        self.count += 1

    def getMedian(self):
		if self.count % 2 == 0:
            return (abs(self.left_heap[0]) + self.right_heap[0]) / 2
        else:
            return abs(self.left_heap[0]) if len(self.left_heap) > len(self.right_heap) else self.right_heap[0]
