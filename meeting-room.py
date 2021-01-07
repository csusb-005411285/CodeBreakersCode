#https://leetcode.com/problems/meeting-rooms/
""""
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

"""
from typing import *

#Attempt 1
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #person can attend the meeting if the intervals are non overlapping
        if not intervals:
            return True
        intervals.sort(key=lambda x: x[0])
        _, cur_end = intervals[0]
        for i in range(1, len(intervals)):
            interval_start, interval_end = intervals[i]
            if interval_start < cur_end:
                return False
            else:
                cur_end = interval_end
        return True

#Attempt 2
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #person can attend the meeting if the intervals are non overlapping
        if not intervals:
            return True
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] > intervals[i+1][0]:
                return False
            i += 1
        return True