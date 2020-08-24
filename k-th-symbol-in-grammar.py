class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        n = N
        k = K

        if n == 1:
            return 0
        
        if n == 2:
            return 0 if k == 1 else 1

        half = 2 ** (n - 2)

        if k <= half:
            return self.kthGrammar(n - 1, k)
        else:
            return int(not self.kthGrammar(n - 1, k - half))  # 1-based index
