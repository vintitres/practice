class Solution:
    def findLHS(self, nums: List[int]) -> int:
        lastv = None
        lastc = None
        mx = 0
        for v, c in sorted(Counter(nums).items()):
            if lastv is not None and v - lastv == 1:
                mx = max(mx, c + lastc)
            lastv = v
            lastc = c
        return mx


        
