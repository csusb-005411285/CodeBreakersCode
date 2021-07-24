class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        mod = pow(10, 9) + 7
        p = [0 for _ in range(n + 1)]
        a = [0 for _ in range(n + 1)]
        l = [0 for _ in range(n + 1)]
        p[0] = 1
        a[0] = 1
        a[1] = 2
        a[2] = 4
        l[0] = 1
        l[1] = 3
        for i in range(1, n):
            p[i] = (a[i - 1] + p[i - 1] + l[i - 1]) % mod
            if i > 1:
                l[i] = (a[i - 1] + p[i - 1] + a[i - 2] + p[i - 2]) % mod
            if i > 2:
                a[i] = (a[i - 1] + a[i - 2] + a[i - 3]) % mod
        return (a[n - 1] + p[n - 1]+ l[n - 1]) % mod
