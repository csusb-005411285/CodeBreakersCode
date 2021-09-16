class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # init dict
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # add a tuple of two values: value and timestamp
        self.time_map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ''
        # apply binary search technique 1
        left = 0
        right = len(self.time_map[key]) - 1 
        arr = self.time_map[key]
        if not arr:
            return ''
        while left <= right:
            mid = left + ((right - left)//2)
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            if arr[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return self.time_map[key][right][1] if right >= 0 else ''
