def dfs(n, consecLate, hasA):
    if n == 0:
        return 1

    tmp = 0
    if not hasA:
        tmp += dfs(n-1, 0, True) # adding A
        tmp %= MOD
    if consecLate < 2:
        tmp += dfs(n-1, consecLate+1, hasA)  # adding L
        tmp %=  MOD
    tmp += dfs(n-1, 0, hasA) # adding P, for every case
    tmp %= MOD 

    return tmp

MOD = 10**9+7
return dfs(n, 0, False)

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
