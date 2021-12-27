# TC: O(n), SC: O(1)
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_without_backspace = self.remove_chars(s)
        t_without_backspace = self.remove_chars(t)
        return (s_without_backspace == t_without_backspace)
    
    def remove_chars(self, string):
        left = 0
        str_list = list(string)
        for right, char in enumerate(str_list):
            if char == '#':
                left -= 1
                left = max(0, left)
            else:
                str_list[left] = str_list[right]
                left += 1
        str_list = str_list[:left]
        return ''.join(str_list)

# Stack       
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_without_backspace = self.remove_char_before_backspace(s)
        t_without_backspace = self.remove_char_before_backspace(t)
        return (s_without_backspace == t_without_backspace)
    
    def remove_char_before_backspace(self, string):
        stack = []
        for i, char in enumerate(string):
            if char == '#' and stack:
                stack.pop()
                continue
            if char != '#':
                stack.append(char)
        return ''.join(stack)
