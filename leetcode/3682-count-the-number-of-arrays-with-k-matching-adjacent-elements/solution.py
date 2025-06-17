class Solution:
    MOD = 10**9 + 7
    def modexcl(n):
        res = 1
        for i in range(1, n + 1):
            res *= i
            res = res % Solution.MOD
        return res
    
    def modinv(n):
        return pow(n, Solution.MOD - 2, Solution.MOD)
    
    def modbicoef(n, k):
        num = Solution.modexcl(n)
        denom = int((Solution.modexcl(k) * Solution.modexcl(n - k)) % Solution.MOD)
        return int((num * Solution.modinv(denom)) % Solution.MOD)

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        if m == 1:
            return 1 if k == n - 1 else 0
        k = n - k - 1
        # how many combinations: x..x y..y x..x y..y x..x y..y of k + 1 sections in n elems
        # how can i pick k split points in n elem array
        # how many combinations of k elements form n - 1 elements
        divisions = Solution.modbicoef(n - 1, k)
        # how many ways can we color k + 1 sections with m colors, but can't have 2 consecutive same colors
        colorings = m * pow(m - 1, k, Solution.MOD)
        return int((divisions * colorings) % Solution.MOD)




        
