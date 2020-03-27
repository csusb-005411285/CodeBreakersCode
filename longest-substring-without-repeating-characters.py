class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0:
      return 0
    # initialize two pointers: start_window and end_window
    start_window, end_window = 0,0
    # initialize a variable to store the max
    _max = 0 
    # initialize a list to store the chars
    chars = []
    # loop through the chars in the string
    for end_window in range(len(s)):
      # if the char is not in the list
      if s[end_window] not in chars:
        # insert it in the list
        chars.append(s[end_window])
        # calculate the max value; it should be the previous max or max length of the list
        _max = max(_max, len(chars))
      # else
      else:
        # get the index of the duplicate element
        index = chars.index(s[end_window])
        # set the start window to this index
        # start_window = start_window if (index < start_window) else index
        for i in range(index, -1, -1):
          value = chars[i]
          chars.remove(value)
          start_window += 1
        # insert the char in the list
        chars.append(s[end_window])
    # return the max value
    return _max
  
  # 2nd attempt
  def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0:
      return 0
    
    if len(s) == 1:
      return 1
    
    # init two pointers
    start = 0
    end = 0
    # init a list to store unique chars
    unique_substr = [] # O(n)
    # init a var to store max length
    max_len = 0
    # loop through the string
    while end < len(s): # O(n2)
      # if char not in unique subsrting
      if s[end] not in unique_substr:
        # add to unique substring
        unique_substr.append(s[end])
        # increment the first pointer
        end += 1
      # else
      else:
        # calculate the max length so far
        # max length is the comparison of exisiting max length vs. length of unique substring
        max_len = max(max_len, len(unique_substr))
        start += 1
        # set the end pointer to the position of the start pointer
        end = start
        # reset the unique substring list
        unique_substr = []
      
    # return the max length     
    return max(max_len, len(unique_substr))
  
  # 3rd attempt. One pointer
  def lengthOfLongestSubstring(self, s: str) -> int:
    # if length of string is 0
    if len(s) == 0:
      # return 0
      return 0
      
    # if length of string is 1
    if len(s) == 1:
      # then return 1
      return 1
    
    # init a pointer
    ptr = 0 # O(1)
    # init a list to store substring
    substr = [] # O(n)
    # init a var to store the max length
    max_len = 0 # O(1)
    # loop through the string
    while ptr < len(s): # O(n)
      # if char not in substring
      if s[ptr] not in substr:
        # insert in substring
        substr.append(s[ptr])
        max_len = max(max_len, len(substr))
      # else
      else:
        # set the max length val
        max_len = max(max_len, len(substr))
        # empty visited
        substr = substr[substr.index(s[ptr]) + 1:]
        # add to visited
        substr.append(s[ptr])
      # increment pointer
      ptr += 1

    # return max length
    return max_len
  
