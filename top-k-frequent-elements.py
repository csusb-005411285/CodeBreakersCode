class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq_map = Counter(nums)
        res = []

        for key, value in freq_map.items(): #

            if len(heap) == k:
                heapq.heappushpop(heap, (value, key)) #
                continue

            heapq.heappush(heap, (value, key)) #

        for i in range(len(heap)):
            res.append(heap[i][1])

        return res # 
