# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/discuss/266550/Python-Stack-O(N)-Solution-with-Explanation

# tc: o(n), sc: o(n)
class Solution:
    def isValid(self, S: str) -> bool:
        if not S:
            return False

        s = S

        while s:
            if s.find('abc') != -1:
                start = s.find('abc')
                end = start + 2 #
                s = s[:start] + s[end + 1:]
            else:
                return False

        return True
