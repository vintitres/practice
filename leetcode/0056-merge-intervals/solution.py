class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: (interval[0], -interval[1]))
        print(intervals)
        if not intervals:
            return []
        new_intervals = []
        last_interval = None
        for interval in intervals:
            if last_interval is None:
                last_interval = interval
            elif interval[0] <= last_interval[1]:
                last_interval[1] = max(last_interval[1], interval[1])
            else:
                new_intervals.append(last_interval)
                last_interval = interval
        new_intervals.append(last_interval)
        return new_intervals

        
