class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        curr_str = ''
        num = 0

        for c in s: 
            if c.isdigit():
                num = (num * 10) + int(c)
            elif c == '[':
                stack.append(curr_str)
                stack.append(num)
                curr_str = ''
                num = 0
            elif c == ']':
                cmb_str = ''
                prev_num = stack.pop()
                prev_str = stack.pop()
                new_str = prev_num * curr_str
                curr_str = prev_str + new_str
            else:
                curr_str += c
    
        return curr_str 
