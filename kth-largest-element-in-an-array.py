class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for i, v in enumerate(nums):
            val = v
            if len(res) == k:
                heappush(res, val)
                heappop(res)
            else:
                heappush(res, val)
        return res[0]
