class Solution:
    def minutes(timePoint: str) -> int:
        hours = int(timePoint[:2])
        minutes = int(timePoint[3:])
        # print(hours, minutes)
        return hours * 60 + minutes

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = sorted(timePoints)
        lastTimePoint = timePoints[0]
        minDiff = Solution.minutes(timePoints[0]) + 60 * 24 - Solution.minutes(timePoints[-1])
        # print(Solution.minutes(timePoints[0]))
        for timePoint in timePoints[1:]:
            # print(Solution.minutes(timePoint))
            # print(minDiff, "D")
            minDiff = min(minDiff, Solution.minutes(timePoint) - Solution.minutes(lastTimePoint))
            if minDiff == 0:
                return 0
            lastTimePoint = timePoint
        return minDiff
        
