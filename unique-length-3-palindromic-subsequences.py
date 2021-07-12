class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = Counter()
        right = Counter(s)
        seen = set()
        for i, char in enumerate(s):
            right[char] -= 1
            for c in string.ascii_lowercase:
                if left[c] > 0 and right[c] > 0:
                    seen.add(c + char)
            left[char] += 1
        return len(seen)
