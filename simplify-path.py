class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_split = path.split('/')
        for i, char in enumerate(path_split):
            if char == '..':
                if stack:
                    stack.pop()
            else:
                if char == '.' or char == '':
                    continue
                stack.append(char)
        return '/' + '/'.join(stack)
