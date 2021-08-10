class MyCalendarThree:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> int:
        self.intervals.append([start,end])
        return self.meeting_room(self.intervals)


    def meeting_room(self,intervals):
        intervals.sort()
        room = []
        _max = 1
        heapq.heappush(room, intervals[0][1])
        for interval in intervals[1:]:
            while room and interval[0] >= room[0]:
                heapq.heappop(room)
            heapq.heappush(room, interval[1])
            _max = max(_max, len(room))
        return _max
