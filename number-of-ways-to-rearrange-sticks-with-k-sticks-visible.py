class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        cache = [[-1 for _ in range(k + 1)] for _ in range(n + 1)] # 1.
        # call recursive method
        self.get_num_arrangements(n, k, cache)
        return cache[-1][-1]
    
    def get_num_arrangements(self, n, k, cache):
        if cache[n][k] != -1:
            return cache[n][k]
        # base case
        if k > n or k == 0: # 2.
            return 0
        if n <= 2: 
            return 1
        arrangements = 0
        modulo = pow(10, 9) + 7
        # choose the max. number
        arrangements = (arrangements + self.get_num_arrangements(n - 1, k - 1, cache)) % modulo
        # do not choose the max. number
        # do not decrement k because we have choosen a number that is not the max, there exists another number that is greater than the current number and it will block this numbers visibility if it is placed to the left of it.
        arrangements = (arrangements + ((n - 1) * self.get_num_arrangements(n - 1, k, cache))) % modulo
        # set the value in cache
        cache[n][k] = arrangements
        # return the sum of two recursive methods
        return arrangements

'''
1. Set to -1 and not 0. Set n to n + 1 and k to k + 1.
2. Weird! This has to come before the next if statement. I don't know why.
'''
     
