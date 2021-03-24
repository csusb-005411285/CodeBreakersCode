class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        last_interval = intervals[0]
        min_intervals = 0
        for i, interval in enumerate(intervals[1:], start=1):
            if interval[0] < last_interval[1]:
                last_interval = interval if last_interval[1] > interval[1] else last_interval
                min_intervals += 1
                continue
            last_interval = interval 
        return min_intervals
