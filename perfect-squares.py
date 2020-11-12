class Solution(object):
    def numSquares(self, n):
        queue = deque()
        queue.append((n, 0))
        visited = [False for _ in range(n + 1)]
        while queue:
            num, count = queue.popleft()
            if num == 0: break
            # n**0.5 = sqrt(n)
            # loop until a number that is square root of n
            for i in range(1, int(num**0.5) + 1):
                # this breaks down to
                # num = (i * i) + (neigh * neigh)
                neigh = num - (i * i)
                # the neighbors of a number are the square roots of the number
                if not visited[neigh]:
                    queue.append((neigh, count + 1))
                visited[neigh] = True 
        return count
