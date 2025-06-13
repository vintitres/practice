class Solution:
    def count(self, prefix: int, n: int):
        print(prefix, n)
        # 1 -> 

    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k = k - 1
        while k > 0:
            first = curr
            last = curr + 1
            # how many between curr and (curr + 1)
            steps = 0
            while first <= n:
                steps += max(0, min(n, last - 1) - first + 1)
                first *= 10
                last *= 10
            # 1 .. 2 - 1 -> 0
            # 10 .. 20 - 1 -> 9
            # 100 .. 200 - 1 -> 99
            # 1000 .. 2000 - 1 -> 999
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        return curr

        
