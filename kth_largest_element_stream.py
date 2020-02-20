class KthLargest:

  def __init__(self, k: int, nums: List[int]):
    # init a heap to store k numbers
    self.heap = nums
    # init a var to store the kth value
    self.k = k
    # convert a list into a heap in linear time
    heapq.heapify(self.heap)
    # if the heap has length greater than k 
    while len(self.heap) > k:
      # remove the smallest element
      heapq.heappop(self.heap)
        
  def add(self, val: int) -> int:
    # if the length of the heap is less than k
    if len(self.heap) < self.k:
      # insert it into the heap
      heapq.heappush(self.heap, val)
    # if the number is greater than the min. value of the heap  
    # and the size of heap is greater than k
    elif val > self.heap[0]:
      # pop the first element
      # insert the new value
      heapq.heapreplace(self.heap, val)
    # return the min. value of the heap
    return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
