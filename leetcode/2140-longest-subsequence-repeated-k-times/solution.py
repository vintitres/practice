class Solution:
    def possible_seq(chars: Dict[chr, int], length: int):
        if length == 0:
            yield ""
            return
        for c in chars.keys():
            if chars[c] > 0:
                chars[c] -= 1
                for seq in Solution.possible_seq(chars, length - 1):
                    yield c + seq
                chars[c] += 1

    def is_rep_seq(seq: str, s_pos: Dict[chr, List[int]], k: str) -> bool:
        # could speed up by generating a char pos lookup dict for s as we do this a lot
        i = 0
        for j in range(k):
            for c in seq:
                j = bisect_left(s_pos[c], i)
                if j == len(s_pos[c]):
                    return False
                i = s_pos[c][j] + 1
        return True

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        chars = {}
        for c, v in reversed(sorted(Counter(s).items())):
            v //= k
            if v > 0:
                chars[c] = v
        b = 0
        e = len(s) // k
        possible = {}
        s_pos = defaultdict(list)
        for i, c in enumerate(s):
            s_pos[c].append(i)
        while b < e:
            m = (b + e + 1) // 2
            possible[m] = False
            for seq in Solution.possible_seq(chars.copy(), m):
                if Solution.is_rep_seq(seq, s_pos, k):
                    possible[m] = seq
                    break
            if possible[m]:
                b = m
            else:
                e = m - 1
        return possible[b] or "" if b in possible else ""
        



        
