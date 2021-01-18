class Solution:
    def __init__(self):
        self.mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.result = []
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self._letterCombinations(0, "", digits)
        return self.result
    
    def _letterCombinations(self, index, current, digits):
        if index == len(digits):
            self.result.append(current)
            return
        letters = self.mapping[int(digits[int(index)])]
        for i in range(len(letters)):
            self._letterCombinations(index + 1, current + letters[i], digits)
        return
