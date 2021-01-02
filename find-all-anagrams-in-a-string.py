class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        right = 0
        char_map = Counter(p)
        chars_encountered = 0
        indices = []
        for right, char in enumerate(s):
            if char in char_map:
                char_map[char] -= 1
                if char_map[char] == 0: 
                    chars_encountered += 1
            while len(s[left: right + 1]) >= len(p) and left <= right:
                if chars_encountered == len(char_map):
                    indices.append(left)
                if s[left] in char_map:
                    if char_map[s[left]] == 0: chars_encountered -= 1
                    char_map[s[left]] += 1
                left += 1
        return indices
