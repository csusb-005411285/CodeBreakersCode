class Solution:
    def isNumber(self, s: str) -> bool:
        curr_state = 1
        states = []
        states = [
            {}, # 0
            {'sign': 2 , 'digit': 8, 'decimal': 9}, # 1
            {'digit': 8, 'decimal': 9}, # 2
            {'digit': 4}, # 3
            {'digit': 4 }, #4
            {'': 6}, #5
            {'sign': 4, 'digit': 4}, #6 Integer state after exp
            {'digit': 7, 'exp': 6}, #7
            {'digit': 8, 'decimal': 7, 'exp': 6}, #8
            {'digit': 7}, #9 same as 7 to handle inputs like +.
        ]
        if s[-1] == "+" or s[-1] == '-' or s[-1] == 'e' or s[-1] == 'E':
            return False
        if s.count('.') == 2 or s.count('e') == 2:
            return False
        for i, char in enumerate(s):
            key = ''
            if char.isdigit():
                key = 'digit'
            elif char == '.':
                key = 'decimal'
            elif char == '+' or char == '-':
                key = 'sign'
            elif char == 'e' or char == 'E':
                key = 'exp'
            if key in states[curr_state]:
                curr_state = states[curr_state][key]
            else:
                return False
        if curr_state in [4, 7, 3, 8]:
            return True
        return False
