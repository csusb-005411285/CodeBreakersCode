class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        result = ''
        for i, char in enumerate(s): 
            if not stack:
                stack.append([char, 1]) 
                continue
            if stack and stack[-1][0] == char: 
                stack[-1][1] += 1 
            else:
                stack.append([char, 1]) 
            if stack and stack[-1][1] == k:
                stack.pop()
        for i, element in enumerate(stack):
            count, char = element
            result += count * char
        return result
