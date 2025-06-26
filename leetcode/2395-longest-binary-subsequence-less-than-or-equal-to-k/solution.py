class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        x = int(s, 2)
        i = 0
        deleted = 0
        bit_n = 1 << (len(s) - 1)
        while x > k:
            while i < len(s) and s[i] == '0':
                i += 1
                bit_n //= 2
            if i == len(s):
                break
            x -= bit_n
            i += 1
            bit_n //= 2
            deleted += 1
        return len(s) - deleted
            


        
