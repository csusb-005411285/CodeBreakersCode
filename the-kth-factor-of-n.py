class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        heap = []
        kth_num = -1
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                heappush(heap, (n//i))
                if (n//i) != i:
                    heappush(heap, (i))
        if len(heap) < k:
            return -1
        while heap and k:
            kth_num = heappop(heap)
            k -= 1
        return kth_num
