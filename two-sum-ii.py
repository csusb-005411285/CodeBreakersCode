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
 
  # 2nd attemp, two pointers
  def twoSum(self, numbers: List[int], target: int) -> List[int]:     
    # if the list has less than one element
    if len(numbers) <= 1:
      # return an empty list
      return []
      
    # init two pointers
    start = 0 # O(1
    end = len(numbers) - 1 # O(1)
    
    # loop through the list
    while(start < end): # O(n)
      if numbers[start] + numbers[end] < target:
        start += 1
      elif numbers[start] + numbers[end] > target:
        end -= 1
      else:
        # if the numbers add up to the target
          # return the index
        return [start + 1, end + 1]
      
    # return empty list
    return []  
        
      
      
        
