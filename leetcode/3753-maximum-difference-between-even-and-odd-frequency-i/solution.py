class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        max_odd = 0
        min_even = 100
        for _, count in freq.items():
            if count % 2 == 1:
                max_odd = max(max_odd, count)
            else:
                min_even = min(min_even, count)
        return max_odd - min_even

        
