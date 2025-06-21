from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = sorted(Counter(word).values())
        begin_sum = 0
        mi = len(word)
        length = len(counts)
        for begin, cb in enumerate(counts):
            end_sum = 0
            for end in reversed(range(begin, length)):
                ce = counts[end]
                if ce - cb <= k:
                    mi = min(mi, begin_sum + end_sum)
                    if end == length - 1:
                        return mi
                    break
                end_sum += ce - (cb + k)
            begin_sum += cb
        return mi
        
