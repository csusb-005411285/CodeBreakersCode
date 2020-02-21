import heapq

class Solution:
  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    # init a heap to store the results
    closest_points_heap = []    
    result = []
    # loop through the list of points
    for x, y in points:
      distance = -(x * x +  y * y)
      # if the length of heap is greater than or equal to k
      if len(closest_points_heap) >= K:
        # if the distance of the point is greater than the first point in the heap
        if distance >= closest_points_heap[0][0]:
          # then insert the point into the heap
          # remove the first element
          heapq.heappushpop(closest_points_heap, (distance, x, y))
        # else
        else:
          # continue
          continue
      # else
      else:
        # insert the point into the heap
        heapq.heappush(closest_points_heap, (distance, x, y))
    # return the result
    for point in closest_points_heap:
      result.append([point[1], point[2]])
    return result
    
