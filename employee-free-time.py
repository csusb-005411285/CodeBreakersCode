'''

                |                    -   |
    |   -   |
                    | - |
    | - |
--------------------------------------------------------------
0   1   2   3   4   5   6   7   8   9   10
'''
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        flattened_schedules = []
        for i, intervals in enumerate(schedule):
            for j, interval in enumerate(intervals):
                flattened_schedules.append(interval)
        flattened_schedules.sort(key = lambda x: x.start)
        common_intervals = []
        free_interval_start_time = flattened_schedules[0].end
        for i, interval in enumerate(flattened_schedules[1:], start = 1):
            if free_interval_start_time >= interval.start:
                free_interval_start_time = max(free_interval_start_time, interval.end)
            else:
                common_intervals.append(Interval(free_interval_start_time, interval.start))
                free_interval_start_time = interval.end
        return common_intervals
