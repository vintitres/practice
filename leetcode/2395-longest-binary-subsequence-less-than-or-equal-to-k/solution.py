class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        x = int(s, 2)
        if x == 0:
            return len(s)
        i = 0
        deleted = 0
        bit_n = 0
        print(s)
        print(bin(x))
        print(bin(bit_n))
        print("w")
        had_one = False
        while x > k:
            while i < len(s) and s[i] == '0':
                i += 1
                if had_one:
                    bit_n //= 2
            if i == len(s):
                break
            if not had_one:
                had_one = True
                bit_n = 1 << (len(s) - i - 1)
                """
            print(bin(bit_n))
            print(bin(x))
            print(i)
            """
            x -= bit_n
            i += 1
            bit_n //= 2
            deleted += 1
        return len(s) - deleted
            


        
