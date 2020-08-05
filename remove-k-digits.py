class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'

        # init a stack
        stack = []
        # insert the first element from num to the stack
        stack.append(num[0])

        # loop through the nums; start from 1
        for i in range(1, len(num)):

            # while k > 0 and the top of the stack is greater than the incoming number:
            while k > 0 and stack and int(stack[-1]) > int(num[i]):
                # pop the element from the top of the stack
                stack.pop()
                # decrement k by 1
                k -= 1

            stack.append(num[i])
        
        if k:
            stack = stack[:-k]
        
        # convert the elements of the stack to string
        num_str = ''.join(stack) 
        # remove leading 0s from the left side of the string and return
        
        return num_str.lstrip('0') or '0'
