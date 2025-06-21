from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = sorted(Counter(word).values())
        begin_sum = 0
        mi = len(word)
        for begin in range(len(counts)):
            end_sum = 0
            for end in reversed(range(begin, len(counts))):
                if counts[end] - counts[begin] <= k:
                    mi = min(mi, begin_sum + end_sum)
                    break
                end_sum += counts[end] - (counts[begin] + k)
            begin_sum += counts[begin]
        return mi
        
