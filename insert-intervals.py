# TC: O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return[newInterval]
        res = []
        # loop
        for k, (curr_start, curr_end) in enumerate(intervals):
            new_start, new_end = newInterval
            # if the new intervals start time is greater than the current intervals end time
            if new_start > curr_end:
                #  append to the result
                res.append([curr_start, curr_end])
            # if the new intervals end time is less than the current intervals start time
            elif new_end < curr_start:
                # insert the new interval and all intervals after the currrent interval
                # needed if the current interval has only 1 elemenet
                k -= 1
                break
            # if the new intervals start time is less than the current intervals end time
            # and the new intervals end time is greater than the current intervals start time
            else:
                # compare the new intervals start time to start time of the current interval
                newInterval[0] = min(new_start, curr_start)
                # compare the end time of new interval with the end time of current interval  
                newInterval[1] = max(new_end, curr_end)
        return res + [newInterval] + intervals[k + 1:]

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
