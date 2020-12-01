class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        count = k
        for i in range(min(k, len(matrix))):
            heappush(heap, (matrix[i][0], 0, matrix[i]))
        while heap and count != 0:
            val, col_index, row = heappop(heap)
            count -= 1
            if col_index + 1 < len(row):
                heappush(heap, (row[col_index + 1], col_index + 1, row))
        return val
