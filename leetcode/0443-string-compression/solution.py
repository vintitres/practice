class Solution:
    def write(self, chars: List[str], j: int, cur: str, ln: int) -> int:
        chars[j] = cur
        j += 1
        if ln > 1:
            for c in str(ln):
                chars[j] = str(c)
                j += 1
        return j

    def compress(self, chars: List[str]) -> int:
        i = 1
        j = 0
        cur = chars[0]
        ln = 1
        while i < len(chars):
            if chars[i] != cur:
                j = self.write(chars, j, cur, ln)
                cur = chars[i]
                ln = 1
            else:
                ln += 1
            i += 1
        j = self.write(chars, j, cur, ln)
        return j


        
