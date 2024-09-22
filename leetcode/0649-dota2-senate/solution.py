class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        banR = 0
        banD = 0
        next_senate = senate
        while True:
            senate = next_senate
            if all(s == 'R' for s in senate):
                return "Radiant"
            if all(s == 'D' for s in senate):
                return "Dire"
            next_senate = ""
            for senator in senate:
                if senator == 'R':
                    if banR > 0:
                        banR -= 1
                    else:
                        next_senate += 'R'
                        banD += 1
                else:
                    if banD > 0:
                        banD -= 1
                    else:
                        next_senate += 'D'
                        banR += 1

        
