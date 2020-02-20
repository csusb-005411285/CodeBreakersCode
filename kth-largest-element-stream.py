class KthLargest:

  def __init__(self, k: int, nums: List[int]):
    # init a heap to hold nums
    self.heap = nums
    # init a var to store the kth value
    self.k = k
    # insert values into the heap
    # use the heapq library
    # how do we solve it without heapq library?
    heapq.heapify(self.heap)
    # pop the smallest numbers before k
    while len(self.heap) > k:
      heapq.heappop(self.heap)
    
  def add(self, val: int) -> int:
    # if the size of heap is less than k
    if len(self.heap) < self.k:  
      # insert value into the heap
      heapq.heappush(self.heap, val)
      # return the top value of the heap
      return self.heap[0]
    # else 
    else:
      if val > self.heap[0]:
        # pop the first element
        # insert the new value
        heapq.heapreplace(self.heap, val)
        # return the top of the heap
        return self.heap[0]
      else:
        # return the max. value of the heap
        return self.heap[0]
    
    return -1
  
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
