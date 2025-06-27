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
        chars = Counter(s)
        for c in chars.keys():
            chars[c] = chars[c] // k
        b = 0
        e = len(s) // k
        possible = {}
        print(chars)
        while b < e:
            m = (b + e + 1) // 2
            print(b, e, m)
            possible[m] = False
            for seq in Solution.possible_seq(chars.copy(), m):
                print(seq)
                if Solution.is_rep_seq(seq, s, k):
                    possible[m] = seq
                    break
            if possible[m]:
                b = m
            else:
                e = m - 1
        print(b, possible)
        return possible[b] or "" if b in possible else ""
        



        
