class Solution:
    def letters(digit: chr) -> List[str]:
        if digit == '1' or digit == '0':
            return ['']
        elif digit == '2':
            return ['a', 'b', 'c']
        elif digit == '3':
            return ['d', 'e', 'f']
        elif digit == '4':
            return ['g', 'h', 'i']
        elif digit == '5':
            return ['j', 'k', 'l']
        elif digit == '6':
            return ['m', 'n', 'o']
        elif digit == '7':
            return ['p', 'q', 'r', 's']
        elif digit == '8':
            return ['t', 'u', 'v']
        elif digit == '9':
            return ['w', 'x', 'y', 'z']
        else:
            raise ValueError(f'Unknown digit {digit}')
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = Solution.letters(digits[0])
        if len(digits) == 1:
            return letters
        combos = []
        for word in self.letterCombinations(digits[1:]):
            for l in letters:
                combos.append(l + word)
        return combos
        
