class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        row = len(mat)
        col = len(mat[0])
        heap = []
        first_item = [0]
        visited = set()
        last_sum = 0
        for row in range(len(mat)):
            first_item[0] += mat[row][0]
            first_item.append(0)
        heappush(heap, tuple(first_item))
        visited.add(tuple(first_item))
        while k > 0:
            last_item = heappop(heap)
            last_sum, indices = last_item[0], last_item[1:]
            for row_idx, col_idx in enumerate(indices):
                next_indices = indices[:row_idx] + tuple([col_idx + 1])  + indices[row_idx + 1:]
                if col_idx + 1 < col and next_indices not in visited:
                    visited.add(next_indices)
                    curr_sum = last_sum - mat[row_idx][col_idx] + mat[row_idx][col_idx + 1]
                    next_item = tuple([curr_sum]) + next_indices
                    heappush(heap, next_item)
            k -= 1
        return last_sum
