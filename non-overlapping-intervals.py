class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 1:
            return 0
        # sort the intervals
        intervals.sort(key=lambda x: x[0])
        # set a reference to the first interval. THis should be a variable.
        ref = intervals[0]
        # set a variable to store the count of overlapping intervals
        no_of_overlapping_intervals = 0
        # loop
        for k, (start_time, end_time) in enumerate(intervals[1:]):
            # for every interval, check:
            prev_start_time, prev_end_time = ref
            # if the reference intervals end time is less than current intervals start time
            if prev_end_time <= start_time:
                # set the reference to the current interval
                ref = [start_time, end_time]
            # if not, it means there is an overlap. Perform these steps:
            else:
                # increment the counter
                no_of_overlapping_intervals += 1
                # check if the reference intervals end time is less than current intervals end time
                # if it is, do not update the reference
                # if not, then set the reference to current interval
                ref = [start_time, end_time] if end_time < prev_end_time else ref
        # return the count 
        return no_of_overlapping_intervals
