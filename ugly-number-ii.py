class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        count = n
        heap.append(1)
        curr = 0
        visited = set()
        while count != 0:
            curr = heappop(heap)
            if curr * 2 not in visited:
                visited.add(curr * 2)
                heappush(heap, curr * 2)
            if curr * 3 not in visited:
                visited.add(curr * 3)
                heappush(heap, curr * 3)
            if curr * 5 not in visited:
                visited.add(curr * 5)
                heappush(heap, curr * 5)
            count -= 1
        return curr 
