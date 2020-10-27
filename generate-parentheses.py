class Solution:
    def __init__(self):
        self.parens = []

    def generateParenthesis(self, n: int) -> [str]:
        self.generate_parenthesis_helper(n, '(', 1, 0)
        return self.parens

    def generate_parenthesis_helper(self, n, curr_combination, open_par, close_par):
        if len(curr_combination) == 2 * n: 
            self.parens.append(curr_combination)
            return
        if open_par < n:
            self.generate_parenthesis_helper(n, curr_combination + '(', open_par + 1, close_par)
        if close_par < open_par:
            self.generate_parenthesis_helper(n, curr_combination + ')', open_par, close_par + 1)
        return
