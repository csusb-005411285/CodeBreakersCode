class RecentCounter:

  def __init__(self):
    # initalize a deque
    self.deque = collections.deque()

  def ping(self, t: int) -> int:
    # insert times into the deque
    self.deque.append(t)
    # if time is less than t-3000 then remove the element
    while (self.deque[0] < t-3000):
      self.deque.popleft()
    # return the number of elements from deque
    return len(self.deque)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
