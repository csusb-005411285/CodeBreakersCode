class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        char_map = defaultdict(int)
        word_map = defaultdict(int)
        left = 0
        right = 0
        max_count = 0
        while right < len(s):
            char = s[right]
            char_map[char] += 1
            while right - left + 1 > minSize and left <= right:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1
            if len(char_map) <= maxLetters and right - left + 1 >= minSize and right - left + 1 <= maxSize:
                word_map[s[left: right + 1]] += 1
            right += 1
        for word, count in word_map.items():
            if max_count < count:
                max_count = count
        return max_count
