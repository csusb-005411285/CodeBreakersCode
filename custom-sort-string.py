class Solution:
    def customSortString(self, S: str, T: str) -> str:
        heap = []
        anagram_t = ''
        char_map = defaultdict(int)
        for i, char in enumerate(S):
            char_map[char] = i
        for i, char in enumerate(T):
            index = float('inf') if char not in char_map else char_map[char]
            heappush(heap, (index, char))
        while heap:
            _, last_char = heappop(heap)
            anagram_t += last_char
        return anagram_t
