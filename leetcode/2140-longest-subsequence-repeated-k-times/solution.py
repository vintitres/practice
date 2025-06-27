class Solution:
    def possible_seq(chars: Dict[chr, int], length: int):
        if length == 0:
            yield ""
            return
        for c in reversed(sorted(chars.keys())):
            if chars[c] > 0:
                chars[c] -= 1
                for seq in Solution.possible_seq(chars, length - 1):
                    yield c + seq
                chars[c] += 1
        return

    def is_rep_seq(seq: str, s: str, k: str) -> bool:
        i = 0
        for j in range(k):
            for c in seq:
                i = s.find(c, i)
                if i == -1:
                    return False
                i += 1
        return True

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        chars = {}
        for c, v in Counter(s).items():
            v //= k
            if v > 0:
                chars[c] = v
        b = 0
        e = len(s) // k
        possible = {}
        while b < e:
            m = (b + e + 1) // 2
            possible[m] = False
            for seq in Solution.possible_seq(chars.copy(), m):
                if Solution.is_rep_seq(seq, s, k):
                    possible[m] = seq
                    break
            if possible[m]:
                b = m
            else:
                e = m - 1
        return possible[b] or "" if b in possible else ""
        



        
