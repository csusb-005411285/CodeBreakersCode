import heapq

class Solution:
    def kClosest(self, points: [[int]], K: int) -> [[int]]:
        heap = []
        res = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = -((x * x) + (y * y))

            if len(heap) == K:
                heapq.heappushpop(heap, (dist, (x, y)))
            else:
                heapq.heappush(heap, (dist, (x, y)))

        for i in range(len(heap)):
            res.append(heap[i][1])
        
        return res
        
