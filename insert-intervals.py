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
