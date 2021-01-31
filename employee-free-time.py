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
        heap = []
        free_times = []
        for i, intervals in enumerate(schedule):
            for interval in intervals:
                heap.append((interval.start, interval.end))
        heapify(heap)
        _, free_interval_start_time = heappop(heap)
        while heap:
            start_time, end_time = heappop(heap)
            if free_interval_start_time < start_time:
                free_times.append(Interval(free_interval_start_time, start_time))
            free_interval_start_time = max(free_interval_start_time, end_time)
        return free_times
