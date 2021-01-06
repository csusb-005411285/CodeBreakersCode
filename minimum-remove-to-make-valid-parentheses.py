class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        char_map = defaultdict(str)
        stack = deque()
        for i, char in enumerate(s):
            char_map[i] = char
        for i, char in enumerate(s):
            if char == '(': stack.append(i)
            if char == ')':
                if stack:
                    last_index = stack.pop()
                    if char_map[last_index] != '(':
                        char_map[i] = ''
                else:
                    char_map[i] = ''
        while stack:
            last_index = stack.pop()
            char_map[last_index] = ''
        return ''.join(char_map.values())
            
