class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_set = set()
        for i, char in enumerate(s):
            if char in char_set:
                char_set.discard(char)
            else:
                char_set.add(char)
        return len(char_set) <= 1
