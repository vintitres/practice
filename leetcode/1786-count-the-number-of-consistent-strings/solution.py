class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set([c for c in allowed])
        consistent = 0
        for word in words:
            ok = True
            for c in word:
                if c not in allowed:
                    ok = False
                    break
            if ok:
                consistent += 1
        return consistent
            
        
