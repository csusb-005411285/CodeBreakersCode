class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i, char in enumerate(s):
            if stack and char == stack[-1]:
                stack.pop()
                continue
            stack.append(char)
        return ''.join(stack)
