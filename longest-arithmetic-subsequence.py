class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A: return 0
        if len(A) == 2: return 2
        dp = [dict() for _ in range(len(A))]
        max_len = float('-inf')
        for i in range(1, len(A)):
            for j in range(i):
                d = A[i] - A[j]
                dp[i][d] = 1+dp[j][d] if d in dp[j] else 2
                max_len = max(max_len, dp[i][d])
        return max_len
