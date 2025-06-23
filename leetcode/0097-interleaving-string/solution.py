class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        is_interleave = [[False] * (len(s2) + 1)] * (len(s1) + 1)
        """
        0, 0, 0: True
        0, 1, 1: 

        """
        for i in range(0, len(s1) + 1):
            for j in range(0, len(s2) + 1):
                if i == 0 and j == 0:
                    is_interleave[0][0] = True
                    continue
                k = i + j
                is_interleave_ij = False
                if i > 0 and s1[i - 1] == s3[k - 1] and is_interleave[i - 1][j]:
                    is_interleave_ij = True
                elif j > 0 and s2[j - 1] == s3[k - 1] and is_interleave[i][j - 1]:
                    is_interleave_ij = True
                is_interleave[i][j] = is_interleave_ij
        print(is_interleave)
        return is_interleave[-1][-1]
        """
        is_interleave[len1, len2, len3] = (s1[len1 - 1] == s3[len3 - 1] and is_interleave[len1 - 1, len2, len3 - 1]) or (s2[len2 - 1] == s3[len3 - 1] and is_interleave[len1, len2 - 1, len3 - 1])
        """
