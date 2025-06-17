class Solution:
    def minMaxDifference(self, num: int) -> int:
        lg = int(log(num, 10))
        tens = 10 ** lg
        mi_first_digit = int(num / tens)
        mx_first_digit = -1
        mi = 0
        mx = 0
        while tens > 0:
            mi *= 10
            mx *= 10
            d = int(int(num / tens) % 10)
            if mx_first_digit == -1 and d != 9:
                mx_first_digit = d
            if d == mx_first_digit:
                mx += 9
            else:
                mx += d
            if d == mi_first_digit:
                mi += 0
            else:
                mi += d
            tens = int(tens / 10)
        return mx - mi

        
