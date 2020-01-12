class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # initialize a hashmap and a List named results
    hashmap = []
    results = []
    # loop through the list
    for i in range(len(nums)):
      # for each element calculate target - element
      if (target - nums[i] in hashmap):
        # if the result of target - element exists in the hashmap then insert the index in result
        index = hashmap.index(target - nums[i])
        results.append(i)
        results.append(index)
        break
      else:
        # else insert the element in the hashmap
        hashmap.append(nums[i])
      
    return results 
        
