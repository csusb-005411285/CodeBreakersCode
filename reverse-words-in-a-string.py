class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_reverse = self.swap_character(s)
        words = self.reverse_words(s_reverse)
        return words

    # o(c), o(1)
    def swap_character(self,  s):
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

    # o(w), o(1)
    def reverse_words(self,  s):
        s = ''.join(s)
        s = s.split(' ')
        result = ''

        for i in s:
            if not i:
                continue

            result += ''. join(self.swap_character(i)) + ' '

        return result.strip()

