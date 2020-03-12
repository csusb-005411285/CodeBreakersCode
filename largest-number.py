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
