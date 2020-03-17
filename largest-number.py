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
