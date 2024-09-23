import math 
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        spells_order = sorted(range(len(spells)), key=lambda i : spells[i])
        pairs = [None] * len(spells)
        last_e = len(potions) - 1
        for spell_id in spells_order:
            need_to_success = math.ceil(success / spells[spell_id])
            b = 0
            e = last_e
            while b <= e:
                m = int(e + b / 2)
                if potions[m] >= need_to_success:
                    e = m - 1
                else:
                    b = m + 1
            pairs[spell_id] = len(potions) - 1 - e
            last_e = e 
        return pairs
        
