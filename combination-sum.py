class Solution:
  # 3rd attempt
  def __init__(self):
    self.unique_combinations = []
  
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    if target == 0 or len(candidates) == 0:
      return []
    
    candidates.sort()
    self.dfs(candidates, target)
    return self.unique_combinations
  
  def dfs(self, candidates, target, next_index = 0, choices = []):
    if target == 0:
      self.unique_combinations.append(choices)
      return
    
    if target < 0:
      return
    
    for i in range(next_index, len(candidates)):
      self.dfs(candidates, target - candidates[i], i, choices + [candidates[i]])
      
# 4th attempt
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        unique_combinations = []
        self.combination_sum_helper(candidates, 0, target, [], unique_combinations)
        return unique_combinations
    
    def combination_sum_helper(self, candidates, start, target, curr_selection = [], unique_combinations = []):
        pprint.pprint(unique_combinations)
        if sum(curr_selection) > target:
            return
        
        if sum(curr_selection) == target:
            unique_combinations.append(curr_selection)
            return

        for i in range(start, len(candidates)):
            self.combination_sum_helper(candidates, i, target, curr_selection + [candidates[i]], unique_combinations)

        return
