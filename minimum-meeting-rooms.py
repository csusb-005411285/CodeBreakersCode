class Meeting:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __lt__(self, other):
    # min heap based on meeting.end
    return self.end < other.end

def min_meeting_rooms(meetings):
    num_meeting_rooms = 1
    # sort the meeting times
    meetings.sort(key=lambda x: x.start)
    # initialize a heapq
    hq = [] 
    # insert first meeting time into the heapq
    ## cannot append item to an empty list when using an heap 
    # loop through the meetings
    for meeting in meetings:
        # for every meeting, check if it overlaps with the meeting in the heapq
        if not hq or meeting.start < hq[0].end:
            # if it does, that means we need another meeting room
            # add the meeting to the heap
            heapq.heappush(hq, meeting)
        else:
            # if it does not
            # remove the meeting times in the priority queue
            # start with the first one and remove all the meeting times that do not overlap
            while hq and meeting.start >= hq[0].end:
                heapq.heappop(hq)
            heapq.heappush(hq, meeting)
        # calculate the total meeting rooms required
        # store the max value
        num_meeting_rooms = max(num_meeting_rooms, len(hq))
    return num_meeting_rooms
