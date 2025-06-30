class Solution:
    THOUSANDS = ["Thousand", "Million", "Billion"] # ... more
    TENS = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    SMALL = ["One", "Two", "Three", "Four", "Five", "Six",
                                   "Seven", "Eight", "Nine", "Ten", "Eleven",
                                   "Twelve", "Thirteen", "Fourteen", "Fifteen",
                                   "Sixteen", "Seventeen", "Eighteen",
                                   "Nineteen"]
    HUNDRED = "Hundred"
    ZERO = "Zero"

    def text_thousand(num: int) -> Optional[str]:
        assert(num >= 0 and num < 1000)
        if num == 0:
            return None
        txt = []
        if num >= 100:
            txt.append(Solution.SMALL[num // 100 - 1] + " Hundred")
        num %= 100
        if num > 0 and num < 20:
            txt.append(Solution.SMALL[num - 1])
        elif num >= 20:
            txt.append(Solution.TENS[num // 10 - 2])
            num %= 10
            if num > 0:
                txt.append(Solution.SMALL[num - 1])
        return " ".join(txt)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return Solution.ZERO
        thousands = []
        thousands_count = 0
        while num > 0:
            str_thousand = Solution.text_thousand(num % 1000)
            num //= 1000
            if str_thousand:
                if thousands_count > 0:
                    str_thousand += " " + Solution.THOUSANDS[thousands_count - 1]
                thousands.append(str_thousand)
            thousands_count += 1
        return " ".join(reversed(thousands))


        
