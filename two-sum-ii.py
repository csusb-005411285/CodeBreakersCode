class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:     
    # if list is less than 1
    if len(numbers) <= 1:
      # then return empty list
      return []
      
    # init a dict
    hashmap = {} # O(n)
    
    # loop through the numbers
    for i in range(len(numbers)): # O(n)
        
      # if the target - num exists in the dict
      if (numbers[i]) in hashmap:
        # get the value 
        num, index = hashmap[numbers[i]]
        # return the stored index and the current non zero index
        return [index, i + 1]
      
      
      # store it in the dict
      # they key should target - num and the value should be number and current non zero index
      hashmap[target - numbers[i]] = [numbers[i], i + 1]
    
    # return empty list
    return []
      
      
      
        
