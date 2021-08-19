class RangeModule:
    
    def __init__(self):
        self.ranges = defaultdict(int)

    def addRange(self, left: int, right: int) -> None:
        # init vars
        key = left
        val = right
        start_times = []
        # loop
        for start, end in self.ranges.items():
            if key <= end and start <= val:
                # update start and end times
                key = min(key, start)
                val = max(val, end)
                # get start time of overlapping interval
                start_times.append(start)
        # remove existing interval
        while start_times:
            start = start_times.pop()
            del self.ranges[start]
        # add new interval 
        self.ranges[key] = val

    def queryRange(self, left: int, right: int) -> bool:
        # loop
        for start, end in self.ranges.items():
            # check if left and right are within any interval ranges
            if start <= left and right <= end:
                return True
        return False
            

    def removeRange(self, left: int, right: int) -> None:
        # vars
        key = left
        val = right
        start_times = []
        # loop
        for start, end in self.ranges.items():
            if key <= end and start <= val:
                # update start and end times
                key = min(key, start)
                val = max(val, end)
                # get start time of overlapping interval
                start_times.append(start)
        # remove existing interval
        while start_times:
            start = start_times.pop()
            del self.ranges[start]
        # add new interval
        if key < left:
            self.ranges[key] = left
        if right < val:
            self.ranges[right] = val
