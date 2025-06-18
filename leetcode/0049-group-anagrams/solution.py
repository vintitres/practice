class Solution:
    def key(s: str) -> str:
        return ''.join(sorted(list(s)))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            k = Solution.key(s)
            if k in groups:
                groups[k].append(s)
            else:
                groups[k] = [s]
        
        return list(groups.values())


        
