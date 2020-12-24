class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_map = Counter(s1)
        left = 0
        right = 0
        for right, char in enumerate(s2):
            if char in char_map:
                char_map[char] -= 1
            while len(s2[left: right + 1]) > len(s1) and left < right:
                if s2[left] in char_map:
                    char_map[s2[left]] += 1
                left += 1    
            if all(not x for x in char_map.values()):
                return True
        return False
