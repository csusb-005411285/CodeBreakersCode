class Solution:
    def calculate(self, s: str) -> int:
        # vars
        stack = []
        operator = '+'
        num = 0
        i = 0
        opset = ('+', '-', '*', '/')
        # init checks
        # processing
        s = s + '+'
        while i < len(s):
            char = s[i]
            #print(char)
            # when num
            if char.isdigit():
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                continue
            # operator
            elif char in opset:
                self.add_to_stack(stack, operator, num)
                num = 0
                operator = char
            elif char == '(':
                stack.append(operator)
                operator = '+'
                num = 0
            elif char == ')':
                self.add_to_stack(stack, operator, num)
                num = 0
                operator = char
                total = 0
                while stack and stack[-1] not in opset:
                    total += stack.pop()
                last_operator = stack.pop()
                self.add_to_stack(stack, last_operator, total)
            i += 1
            #print(stack)
        return sum(stack)
        
    # helper
    def add_to_stack(self, stack, op, num):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(stack.pop() * num)
        elif op == '/':
            stack.append(int(stack.pop() / num))
