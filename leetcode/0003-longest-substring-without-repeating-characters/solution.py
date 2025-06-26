class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: Dict[char, int] = {}
        mx = 0
        word_start = 0
        for i, c in enumerate(s):
            if c in last_seen:
                word_start = max(word_start, last_seen[c] + 1)
            last_seen[c] = i
            print(i, i - word_start + 1)
            mx = max(mx, i - word_start + 1)
        return mx

        
