class Solution:
    def __init__(self):
        self.output_list = set()
        self.max_str_len = 0
        self.cache = defaultdict(str)
        
    def check_valid_parentheses(self, s):
        stack = []
        for p in s:
            if p == '(':
                stack.append(p)
            if p == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        return True if not stack else False

    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        self._remove_invalid_parenthesis(s)
        return list(filter(lambda x: len(x) == self.max_str_len, self.output_list))

    def _remove_invalid_parenthesis(self, s):
        if s in self.cache:
            self.output_list.add(self.cache[s])
            return
        if not s:
            return []
        if self.check_valid_parentheses(s):
            self.output_list.add(s)
            self.max_str_len = max(self.max_str_len, len(s))
        for i in range(len(s)):
            new_str = s[:i] + s[i + 1:]
            if self.check_valid_parentheses(new_str):
                self.cache[new_str] = new_str
                self.output_list.add(new_str)
                self.max_str_len = max(self.max_str_len, len(new_str))
            self._remove_invalid_parenthesis(new_str)
        self.cache[s] = '' if s not in self.cache else self.cache
        return
        
