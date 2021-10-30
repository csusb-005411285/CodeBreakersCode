class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[0])
        cache = defaultdict(int)
        return self.get_max_sum(events, 0, 0, k, 0, cache)
    
    def get_max_sum(self, events, i, j, k, last_event_end_time, cache): 
        if (i, j, last_event_end_time) in cache:
            return cache[(i, j, last_event_end_time)]
        # base case
        if i >= len(events): 
            return 0
        if j == k: 
            return 0
        # if current event start time lesser than or equal to the last event end time
        # then the events overlap
        event = events[i] 
        if event[0] <= last_event_end_time:
            # skip current event
            return self.get_max_sum(events, i + 1, j, k, last_event_end_time, cache) # 2.
        # include 
        # add the current value, increment i, increment k, add the end time
        attend = self.get_max_sum(events, i + 1, j + 1, k, events[i][1], cache) + events[i][2] # 7
        # exclude
        # increment i, do not increment k, do not add current value
        skip = self.get_max_sum(events, i + 1, j, k, last_event_end_time, cache) # 1. 
        # return max of include and exclude
        cache[(i, j, last_event_end_time)] = max(attend, skip)
        return cache[(i, j, last_event_end_time)]

'''
1. The event end time should be `last_event_end_time` and not events[i][1] as we are not including the current event in this recursive call.
2. The current event overlaps with the previous event, so we cannot attend this event. Skip this event.
'''
