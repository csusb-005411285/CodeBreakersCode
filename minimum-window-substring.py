class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_map = Counter(t)
        char_found = 0
        subsequence = s
        left = 0
        for right, char in enumerate(s):
            if char in char_map:
                char_map[char] -= 1
                if char_map[char] == 0:
                    char_found += 1
            while char_found == len(char_map) and left <= right:
                if len(subsequence) > right - left + 1:
                    subsequence = s[left: right + 1]
                if s[left] in char_map:
                    if char_map[s[left]] == 0:
                        char_found -= 1
                    char_map[s[left]] += 1
                    left += 1
                while left < len(s) and s[left] not in char_map:
                    left += 1
        return subsequence if left != 0 and right != len(s) else ''
