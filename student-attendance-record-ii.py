class Solution:
    def checkRecord(self, n: int) -> int:
        cache = defaultdict(int)
        return self._check_record(n, 0, 0, 0, 0, cache)
    
    def _check_record(self, n, a, l, p, i, cache):
        if (i, a, l) in cache: # 1. 
            return cache[(i, a, l)]
        # base case
        # if i equals n
        if i == n:
            return 1
        modulo = pow(10, 9) + 7
        # add p
        count = self._check_record(n, a, 0, p + 1, i + 1, cache) # 2.
        # add a
        if a < 1:
            count += self._check_record(n, 1, 0, p, i + 1, cache) # 2.
        # add l
        if l < 2:
            count += self._check_record(n, a, l + 1, p, i + 1, cache)
        # return sum of three calls
        cache[(i, a, l)] = count % modulo
        return cache[(i, a, l)]
    
'''
1. cache should only have a, i, l as these three variables are bounded by a condition. Adding 'p' to it will result in an error.
2. the value of l has to be 0; not sure why it is this way. 
'''

# bottom-up solution. TLE.
class Solution:
    def checkRecord(self, n: int) -> int:
        cache = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)] 
        cache[0] = [[1, 1, 1], [1, 1, 1]]
        modulo = pow(10, 9) + 7
        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    val = cache[i - 1][j][2] % modulo
                    if j > 0:
                        val = (val + cache[i - 1][j - 1][2]) % modulo # 2.
                    if k > 0:
                        val = (val + cache[i - 1][j][k - 1]) % modulo # 3.
                    cache[i][j][k] = val
        return cache[n][1][2] # 1.
'''
1. Last row, last col, and last inner row
2. to calculate a
3. to calculate l
'''

public int checkRecord(int n) {
        int[][][] mem = new int[n][2][3];
        return dfs(0, 0, 0, n, mem);   
    }
    private int dfs(int i, int A, int L, int n, int[][][] mem) {
        if(i==n) return 1;
        if(mem[i][A][L]!=0) return mem[i][A][L];
        long res = dfs(i+1, A, 0, n, mem);  //P
        if(A==0) res += dfs(i+1, 1, 0, n, mem); //A
        if(L<2) res += dfs(i+1, A, L+1, n, mem); //L
        return mem[i][A][L] = (int)(res%1000000007);
    }
}

public int checkRecord(int n) {
        int[][][] dp = new int[n+1][2][3];
        dp[n]=new int[][]{{1,1,1},{1,1,1}};
        int mod = 1000000007;
        for(int i=n-1;i>=0;i--) 
            for(int A=0; A<2;A++)
                for(int L=0;L<3;L++) {
                    dp[i][A][L] = dp[i+1][A][0];
                    if(A==0) dp[i][0][L] = (dp[i][0][L]+dp[i+1][1][0])%mod;
                    if(L<2) dp[i][A][L] = (dp[i][A][L]+dp[i+1][A][L+1])%mod;
                }        
        return dp[0][0][0];   
    }
