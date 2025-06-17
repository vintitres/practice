class Solution:
    def first_digit_but(num, but):
        digit = -1
        while num > 0:
            d = int(num % 10)
            num = int(num / 10)
            if d not in but:
                digit = d
        return digit

    def maxDiff(self, num: int) -> int:
        min_x = Solution.first_digit_but(num, {})
        min_y = 1
        if min_x == 1:
            min_x = Solution.first_digit_but(num, {0, 1})
            min_y = 0
        max_x = Solution.first_digit_but(num, {9})
        print(min_x, min_y, max_x)
        a = 0
        b = 0
        tens = 10 ** int(log(num, 10))
        while tens > 0:
            d = int(int(num / tens) % 10)
            a *= 10
            b *= 10
            a += (d if d != min_x else min_y)
            b += (d if d != max_x else 9)
            tens = int(tens / 10)
        print(b, a)
        return b - a

        
