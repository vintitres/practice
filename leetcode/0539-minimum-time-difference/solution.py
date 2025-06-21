class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = sorted(int(point[0:2]) * 60 + int(point[3:5]) for point in timePoints)
        minDiff = 24 * 60 - timePoints[-1] + timePoints[0]
        lastPoint = timePoints[0]
        for point in timePoints[1:]:
            minDiff = min(minDiff, point - lastPoint)
            lastPoint = point
        return minDiff
