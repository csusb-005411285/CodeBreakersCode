import heapq

class Solution:
  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    # init a heap to store the closest points
    heap = []

    # loop through the points
    for (x, y) in points:
      # calculate the distance between the origin and the point
      # the formula is x**2 + y**2 ?
      # the - is only because python's heapq sorts elements in increasing order
      dist = -(x*x + y*y)
      # if the heap is full
      if len(heap) == K:
        # insert and pop element
        heapq.heappushpop(heap, (dist, x, y))
      else:
        # insert eement
        heapq.heappush(heap, (dist, x, y))
      # return the points   
      return [(x,y) for (dist,x, y) in heap]
