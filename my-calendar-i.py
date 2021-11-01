class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        if not self.events:
            self.events.append((start, end)) 
            return True
        indx = self.find_index(start) 
        if indx - 1 >= 0 and self.events[indx - 1][1] > start:
            return False
        if (indx < len(self.events) and end > self.events[indx][0]):
            return False
        if indx == len(self.events):
            self.events.append((start, end))
        else:
            self.events.insert(indx, (start, end))
        return True
    
    def find_index(self, target): 
        left = 0
        right = len(self.events) - 1 
        while left <= right: 
            mid = left + (right - left)//2
            if self.events[mid][0] <= target: 
                left = mid + 1
            else:
                right = mid - 1
        return left 
    
class MyCalendar:

    def __init__(self):
        self.calendar = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        can_book = True
        for prev_start, prev_end in self.calendar.items():
            if start < prev_end and prev_start < end:
                can_book = False
                break
        if can_book:
            self.calendar[start] = end
        return can_book
