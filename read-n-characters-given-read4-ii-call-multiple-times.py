class Solution:
    def __init__(self):
        self.buff = [''] * 4
        self.received_chars = 0
        self.buffer_index = 0

    def read(self, buf: List[str], n: int) -> int:
        count = 0
        while count < n:
            if self.buffer_index >= self.received_chars:
                self.buffer_index = 0
                self.received_chars = read4(self.buff)
                if self.received_chars == 0:
                    break
            buf[count] = self.buff[self.buffer_index]
            count += 1
            self.buffer_index += 1
        return count
