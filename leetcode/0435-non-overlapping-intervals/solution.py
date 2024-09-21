from heapq import heappop, heappush
from sortedcontainers import SortedSet

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = [(interval[1], interval[0]) for interval in intervals]
        intervals.sort()
        prev_end = -600000
        count = 0
        for (end, start) in intervals:
            if start >= prev_end:
                count += 1
                prev_end = end
        return len(intervals) - count

        
