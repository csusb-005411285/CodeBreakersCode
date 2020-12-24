class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return t
        char_map = Counter(t)
        left = 0
        substr_found = 0
        substr = s
        for right, char in enumerate(s):
            if char in char_map:
                char_map[char] -= 1
                if char_map[char] == 0: substr_found += 1
            while substr_found == len(char_map.keys()) and left <= right:
                if len(s[left: right + 1]) < len(substr):
                    substr = s[left: right + 1]
                if s[left] not in char_map:
                    left += 1
                    continue
                else:
                    char_map[s[left]] += 1
                    if char_map[s[left]] > 0: substr_found -= 1
                    left += 1
        return substr if left != 0 and right != len(s) else ''
