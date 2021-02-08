class Solution:
    def __init__(self):
        self.all_possible = set()
        self.max_len = 0

    def is_valid_parentheses(self, s):
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        return True if not stack else False

    def removeInvalidParentheses(self, s: str) -> List[str]:
        cache = defaultdict(str)
        self._remove_invalid_parentheses(s, cache)
        return list(filter(lambda x: len(x) == self.max_len, self.all_possible))
    
    def _remove_invalid_parentheses(self, s, cache):
        if s in cache:
            self.all_possible.add(cache[s])
            return
        if not s:
            self.all_possible.add('')
            return 
        if self.is_valid_parentheses(s):
            if len(s) >= self.max_len:
                self.max_len = len(s)
                self.all_possible.add(s)
                cache[s] = s
                return
        for i, char in enumerate(s):
            new_string = s[:i] + s[i + 1:]
            self._remove_invalid_parentheses(new_string, cache)
        if s not in cache:
            cache[s] = ''
        return
