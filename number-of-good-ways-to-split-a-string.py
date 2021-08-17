class Solution:
    def numSplits(self, s: str) -> int:
        end = Counter(s)
        start = defaultdict(int)
        count = 0
        for char in s:
            start[char] += 1
            end[char] -= 1
            if end[char] == 0:
                del end[char]
            if len(start) == len(end):
                count += 1
        return count
