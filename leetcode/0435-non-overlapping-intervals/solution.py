from heapq import heappop, heappush
from sortedcontainers import SortedSet

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[1])
        prev_end = -600000
        count = 0
        for (start, end) in intervals:
            if start >= prev_end:
                count += 1
                prev_end = end
        return len(intervals) - count

        
