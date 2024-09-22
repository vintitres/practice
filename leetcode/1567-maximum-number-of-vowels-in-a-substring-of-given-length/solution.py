class Solution:
    VOWELS = set(['a', 'e', 'i', 'o', 'u'])
    def is_vowel(self, c: chr) -> bool:
        return c in self.VOWELS
    def maxVowels(self, s: str, k: int) -> int:
        vovels = 0
        mx = 0
        for i, c in enumerate(s):
            if self.is_vowel(c):
                vovels += 1
            if i - k >= 0 and self.is_vowel(s[i - k]):
                vovels -= 1
            mx = max(mx, vovels)
        return mx

        
