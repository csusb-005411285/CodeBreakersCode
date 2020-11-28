'''
O(n * prime * log n) O(n)
'''
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: [int]) -> int:
        heap = []
        count = n
        heap.append(1)
        curr = 0
        visited = set()
        while count != 0:
            curr = heappop(heap)
            for prime in primes:
                if curr * prime not in visited:
                    visited.add(curr * prime)
                    heappush(heap, curr * prime)
            count -= 1
        return curr 
