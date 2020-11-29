class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = []
        if not nums1 or not nums2: return []
        for i in range(min(k, len(nums1))):
            heappush(heap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
        while heap and len(res) < k:
            sum_val, val_num1, val_num2, index_num2 = heappop(heap)
            res.append([val_num1, val_num2])
            if index_num2 < len(nums2) - 1:
                next_index = index_num2 + 1
                heappush(heap, (val_num1 + nums2[next_index], val_num1, nums2[next_index], next_index))
        return res
