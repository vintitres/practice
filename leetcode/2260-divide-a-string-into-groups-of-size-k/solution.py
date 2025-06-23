class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = []
        for i in range(math.ceil(len(s) / k)):
            ret.append(s[i * k:i * k + k])
        if len(ret[-1]) < k:
            ret[-1] = ret[-1] + fill * (k - len(ret[-1]))
        return ret
        
