class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = defaultdict(int)
        max_len = 0
        right, left = 0, 0
        for right, c in enumerate(s):
            char_map[c] += 1
            while (len(s[left: right + 1]) - max(char_map.values())) > k:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0: del char_map[s[left]]
                left += 1
            max_len = max(max_len, len(s[left: right + 1]))
        return max_len
