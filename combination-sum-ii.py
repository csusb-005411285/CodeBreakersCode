class Solution:
    def __init__(self):
        self.combination_sum = []

    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        candidates.sort()
        self.combination_sum_helper(candidates, target, 0, [])
        return self.combination_sum
    
    def combination_sum_helper(self, candidates, target, index, curr_comb):
        if sum(curr_comb) > target:
            return
        if sum(curr_comb) == target:
            self.combination_sum.append(curr_comb)
            return
        for i in range(index, len(candidates)):
            if i == index or candidates[i - 1] != candidates[i]:
                self.combination_sum_helper(candidates, target, i + 1, curr_comb + [candidates[i]])
        return 
