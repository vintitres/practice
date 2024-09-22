class Solution:
    """
    8: 1000
    3: 0011
    5: 0101

    a   : 10010101
    c   : 10000011
    a   : 10010101
    ~c  : 01111100
    a&~c: 00010100
    """
    def minFlips(self, a: int, b: int, c: int) -> int:
        aorbto1 = (((a | b) & c) ^ c).bit_count()
        ato0 = (a & ~c).bit_count()
        bto0 = (b & ~c).bit_count()
        return aorbto1 + ato0 + bto0

