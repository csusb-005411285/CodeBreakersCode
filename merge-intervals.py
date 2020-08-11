class Solution:
  def merge(self, intervals: [[int]]) -> [[int]]:
    if not intervals:
        return []

    # sort by end times
    intervals.sort(key = lambda x: x[0]) # [[1,3],[2,6],[8,10],[15,18]]
    # init a var to store the non-overlapping times
    res = [intervals[0]] # [1, 3]

    # loop through the intervals
    for i in range(1, len(intervals)): # 2

        # if the intervals overlap
        # check the current interval and the last interval in the var
        if res[-1][1] >= intervals[i][0]: # 6 >=10 
            if res[-1][1] <= intervals[i][1]: # 3 <= 6
                res[-1][1] = intervals[i][1] # [1, 6]
            
            if res[-1][0] >= intervals[i][0]:
                res[-1][0] = intervals[i][0]
        else:
            res.append(intervals[i])

    return res
