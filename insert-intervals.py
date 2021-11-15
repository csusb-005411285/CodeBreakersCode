# TC: O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals_after_intersection = []
        i = 0
        new_interval_start, new_interval_end = newInterval
        while i < len(intervals) and intervals[i][0] < new_interval_start:
            intervals_after_intersection.append(intervals[i])
            i += 1
        if not intervals_after_intersection or intervals_after_intersection[-1][1] < new_interval_start:
            intervals_after_intersection.append(newInterval)
        else:
            intervals_after_intersection[-1][1] = max(intervals_after_intersection[-1][1], new_interval_end)
        while i < len(intervals):
            if intervals_after_intersection[-1][1] >= intervals[i][0]:
                intervals_after_intersection[-1][1] = max(intervals_after_intersection[-1][1], intervals[i][1])
            else:
                intervals_after_intersection.append(intervals[i])
            i += 1
        return intervals_after_intersection

# TC: O(nlogn)
class Solution:
    def insert(self, intervals: [[int]], newInterval) -> [[int]]:
        if not intervals and newInterval: return[newInterval]
        res = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        res.append(intervals[0]) 
        for k, (curr_start, curr_end) in enumerate(intervals[1:]): 
            prev_start, prev_end = res[-1] 
            if prev_end >= curr_start: 
                res[-1][1] = max(prev_end, curr_end) 
            else:
                res.append([curr_start, curr_end])
        return res
