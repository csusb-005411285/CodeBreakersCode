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
