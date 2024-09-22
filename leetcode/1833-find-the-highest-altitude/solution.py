class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = altitude
        for g in gain:
            altitude += g
            highest = max(highest, altitude)
        return highest
        
