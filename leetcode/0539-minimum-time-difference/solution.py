class Solution:
    def minutes(timePoint: str) -> int:
        hours = int(timePoint[:2])
        minutes = int(timePoint[3:])
        # print(hours, minutes)
        return hours * 60 + minutes

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [Solution.minutes(tp) for tp in sorted(timePoints)]
        lastTimePoint = timePoints[0]
        minDiff = timePoints[0] + 60 * 24 - timePoints[-1]
        # print(Solution.minutes(timePoints[0]))
        for timePoint in timePoints[1:]:
            # print(Solution.minutes(timePoint))
            # print(minDiff, "D")
            minDiff = min(minDiff, timePoint - lastTimePoint)
            if minDiff == 0:
                return 0
            lastTimePoint = timePoint
        return minDiff
        
