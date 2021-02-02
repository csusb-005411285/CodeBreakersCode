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
        all_schedules = []
        free_times = []
        for i, intervals in enumerate(schedule):
            for j, interval in enumerate(intervals):
                all_schedules.append(interval)
        all_schedules.sort(key=lambda x: x.start)
        last_free_interval_end_time = all_schedules[0].end
        for k, interval in enumerate(all_schedules[1:], start=1):
            if last_free_interval_end_time < interval.start:
                free_times.append(Interval(last_free_interval_end_time, interval.start))
            last_free_interval_end_time = max(last_free_interval_end_time, interval.end)
        return free_times
