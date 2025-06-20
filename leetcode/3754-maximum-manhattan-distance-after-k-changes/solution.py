from collections import defaultdict

class Solution:
    def max_with_flip(d1: int, d2: int, k: int) -> (int, int):
        longer = max(d1, d2)
        shorter = min(d1, d2)
        flipped = min(shorter, k)
        dist = longer + flipped - (shorter - flipped)
        new_k = k - flipped
        return (dist, new_k)

    def maxDistance(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        mx = 0
        for c in s:
            cnt[c] += 1
            ns_dist, kk = Solution.max_with_flip(cnt['N'], cnt['S'], k)
            we_dist, _ = Solution.max_with_flip(cnt['W'], cnt['E'], kk)
            mx = max(mx, ns_dist + we_dist)
        return mx

        
