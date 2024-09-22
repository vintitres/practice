class Solution:
    """
    8: 1000
    3: 0011
    5: 0101
    """
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            abit = a % 2
            bbit = b % 2
            cbit = c % 2
            # print(abit, bbit, cbit)
            if cbit == 0:
                flips += abit + bbit
            elif abit == 0 and bbit == 0:
                flips += 1
            a = int(a / 2)
            b = int(b / 2)
            c = int(c / 2)
        return flips 
