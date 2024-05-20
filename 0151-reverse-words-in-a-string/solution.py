class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(filter(lambda w : w != "", s.split(" ")))
        l.reverse()
        return " ".join(l)
