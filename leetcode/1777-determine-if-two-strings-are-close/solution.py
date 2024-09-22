class Solution:
    def charCounts(self, word: str) -> (List[int], Set[chr]):
        counts = {chr(ord('a') + c): 0 for c in range(26)}
        chars = set()
        for c in word:
            counts[c] += 1
            chars.add(c)
        return (sorted(counts.values()), chars)

    def closeStrings(self, word1: str, word2: str) -> bool:
        return self.charCounts(word1) == self.charCounts(word2)
        
