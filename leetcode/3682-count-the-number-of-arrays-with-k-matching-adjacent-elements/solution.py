class Solution:
    def modpow(base, power, mod):
        res = 1 
        subpow = base
        while power > 0:
            if int(power % 2) == 1:
                res *= subpow
                res = int(res % mod)
            power /= 2
            subpow *= subpow
            subpow = int(subpow % mod)
        return res

    def modexcl(n, mod):
        res = 1
        for i in range(1, n + 1):
            res *= i
            res = int(res % mod)
        return res
    
    def modinv(n, mod):
        return Solution.modpow(n, mod - 2, mod)
    
    def modbicoef(n, k, mod):
        print(n, k)
        num = Solution.modexcl(n, mod)
        denom = int((Solution.modexcl(k, mod) * Solution.modexcl(n - k, mod)) % mod)
        return int((num * Solution.modinv(denom, mod)) % mod)

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        if m == 1:
            return 1 if k == n - 1 else 0
        k = n - k - 1
        # how many combinations: x..x y..y x..x y..y x..x y..y of k + 1 sections in n elems
        # how can i pick k split points in n elem array
        # how many combinations of k elements form n - 1 elements
        divisions = Solution.modbicoef(n - 1, k, mod)
        # how many ways can we color k + 1 sections with m colors, but can't have 2 consecutive same colors
        colorings = m * Solution.modpow(m - 1, k, mod)
        print(divisions, colorings)
        return int((divisions * colorings) % mod)




        
