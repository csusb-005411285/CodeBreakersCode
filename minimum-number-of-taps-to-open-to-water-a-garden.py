class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = [0] * (n + 1)
        max_range = 0
        next_pos = 0
        tap = 0
        for i, val in enumerate(ranges):
            index = max(0, i - val)
            right_index = max(taps[index], i + val)
            taps[index] = right_index
        for i, val in enumerate(taps):
            if next_pos >= len(taps) - 1:
                break
            if i > max_range:
                return -1
            max_range = max(max_range, val)
            if i == next_pos:
                next_pos = max(next_pos, max_range)
                tap += 1
        return tap
