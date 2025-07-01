class Solution:
    def possibleStringCount(self, word: str) -> int:
        last_chr = '-'
        last_chr_count = 0
        ret = 0
        for c in word:
            if last_chr != c:
                if last_chr_count > 1:
                    print(last_chr_count)
                    ret += last_chr_count - 1
                last_chr = c
                last_chr_count = 1
            else:
                last_chr_count += 1
        if last_chr_count > 1:
            ret += last_chr_count - 1
        return ret + 1
        
