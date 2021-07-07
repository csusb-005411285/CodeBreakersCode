class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        original = x
        while x:
            x, remainder = divmod(x, 10)
            reverse = reverse * 10 + remainder
        return reverse == original
