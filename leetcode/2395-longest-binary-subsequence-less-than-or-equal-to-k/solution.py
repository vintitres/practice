class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        x = int(s, 2)
        i = 0
        deleted = 0
        bit_n = 1 << (len(s) - 1)
        if x <= k:
            return len(s)
        for bit in s:
            if bit == '1':
                x -= bit_n
                deleted += 1
                if x <= k:
                    return len(s) - deleted
            bit_n //= 2
        return -1
            


            


        
