class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        happy_str_arr = []
        heap = []
        if a != 0:
            heappush(heap, (-a, 'a'))
        if b != 0:
            heappush(heap, (-b, 'b'))
        if c != 0:
            heappush(heap, (-c, 'c'))
        while heap:
            first_char_count, first_char = heappop(heap)
            if len(happy_str_arr) > 1 and happy_str_arr[-1] == happy_str_arr[-2] == first_char:
                if not heap:
                    return ''.join(happy_str_arr)
                sec_char_count, sec_char = heappop(heap)
                happy_str_arr.append(sec_char)
                sec_char_count += 1
                if sec_char_count != 0:
                    heappush(heap, (sec_char_count, sec_char))
                heappush(heap, (first_char_count, first_char))
                continue
            happy_str_arr.append(first_char)
            first_char_count += 1
            if first_char_count != 0:
                heappush(heap, (first_char_count, first_char))
        return ''.join(happy_str_arr)
