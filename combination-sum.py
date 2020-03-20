class Solution:
  
  def __init__(self):
    # init a var to store the results
    self.results = []
  
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    # call dfs using with the current index of 0, current choices as empty list
    # result as empty list
    self.dfs(candidates, target, 0, [])
    return self.results
    
  def dfs(self, candidates, target, curr_index, curr_choices=[]):
    # check if the target is less than 0
    if target < 0:
      # backtrack
      return
    
    # if the target is 0
    if target == 0:
      # then add it to the result
      self.results.append(curr_choices)
      return
    
    # loop through the candidates 
    for i in range(curr_index, len(candidates)):
      # for each candidate, reduce the target by the value of the candidate
      choices = curr_choices + [candidates[i]]
      self.dfs(candidates, target-candidates[i], i, choices)
      
  # 2nd attempt
  def __init__(self):
    self.results = [] # O(n)
  
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    if len(candidates) == 0:
      return []
    
    candidates.sort()
    self.dfs(candidates, target, 0, [])
    return self.results
  
  def dfs(self, candidates, target, index, choices):
    if target == 0:
      self.results.append(choices)
      return 
    
    if target < 0:
      return;
    
    for i in range(index, len(candidates)): # O(n)
      self.dfs(candidates, target - candidates[i], i, choices + [candidates[i]]) #O(n)
