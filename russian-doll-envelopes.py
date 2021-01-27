class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        sorted_envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        cache = []
        heights = [sorted_envelopes[i][1] for i in range(len(sorted_envelopes))]
        for i, num in enumerate(heights):
            index = bisect_left(cache, num)
            if index == len(cache) or not cache:
                cache.append(num)
            else:
        return len(cache)
