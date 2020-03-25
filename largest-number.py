import functools

class Solution:
  def largestNumber(self, nums: List[int]) -> str:
    if len(nums) == 0:
      return ''
    
    if len(nums) == 1:
      return str(nums[0])
    
    # init a var to store results
    result = ''
    # convert the list to a list of strings
    int_to_str = map(str, nums)
    # sort the list of strings by comparing the sum
    sorted_nums = sorted(int_to_str, key=functools.cmp_to_key(lambda str1, str2: -1 if str1+str2 > str2+str1 else(1 if str1+str2 < str2+str1 else 0)))
    # combine the elements of the list
    result = ''.join(sorted_nums)
    # return the result
    return result.lstrip("0") or "0"

  # 3rd attempt. Selection sort
  def largestNumber(self, nums: List[int]) -> str:
    if len(nums) == 0:
      return ''
    if len(nums) == 1:
      return str(nums[0])
    
    # init a list to store the list of strings
    str_list = list(map(str, nums))
    # init a var to store the min value
    max_index = 0
    # init a var to store the results
    results = ''
    # loop through the list
    for i in range(len(str_list)):
      max_index = i
      for j in range(i + 1, len(str_list)):
        # compare the concatenation of two strings and sort them
        if str_list[max_index] + str_list[j] < str_list[j] + str_list[max_index]:
          max_index = j
      str_list[i], str_list[max_index] = str_list[max_index], str_list[i]
    # join the elements of the list
    results = ''.join(str_list)
    # check for leading 0s
    return results.lstrip('0') or '0'
 
  # 4th attempt
  def largestNumber(self, nums: List[int]) -> str:
    if len(nums) == 0:
      return ''
    
    if len(nums) == 1:
      return str(nums[0])
    
    # init a list to store the integers in a list of strings
    nums_str = list(map(str, nums)) # O(n)
    
    # perform merge sort
    result = self.merge_sort(nums_str) # O(n)

    # left strip 0's or return 0
    return ''.join(result).lstrip('0') or '0'
  
  def merge_sort(self, nums: List[str]) -> List[str]:
    # if the length of str is 1
    if len(nums) == 1:
      # then return the str
      return nums
    
    # find the mid point
    mid = len(nums) // 2
    
    # calculate the left and right half
    left = self.merge_sort(nums[:mid])
    right = self.merge_sort(nums[mid:])    

    # return the combined list
    return self.combine(left, right)
    
  def combine(self, left: List[str], right: List[str]) -> List[str]:
    # init the left and right pointer
    left_ptr = 0 # O(1)
    right_ptr = 0 # O(1)
    # init a var to store the results
    results = [] # O(n)

    # if the length of left and right list is 1
    if len(left) == 1 and len(right) == 1:
      # return the sorted list
      return [left[0], right[0]] if left[0] + right[0] > right[0] + left[0] else [right[0], left[0]]
    
    # loop through both the lists simultaneously
    while left_ptr < len(left) and right_ptr < len(right):
      # if left element is greater than the right
      if left[left_ptr] + right[right_ptr] > right[right_ptr] + left[left_ptr]:
        # insert it in the result
        results.append(left[left_ptr])
        # increment the left pointer
        left_ptr += 1
      # else
      else:
        # insert it in the result
        results.append(right[right_ptr])
        # increment the right pointer
        right_ptr += 1
        
    # if the left or right list has leftover elements
    if left_ptr < len(left):
      # then append it to the result list
      results.extend(left[left_ptr:])
      
    if right_ptr < len(right):
      results.extend(right[right_ptr:])
      
    # return the result
    return results
