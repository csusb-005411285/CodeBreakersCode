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
  
  # O(1) space O(n) time
  def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0:
      return 0
    
    if len(s) == 1:
      return 1
    
    # init two pointers
    start = 0 # O(1)
    end = 0 # O(1)
    # init a var to store the result
    max_len = 0 # O(1)
    
    # loop through the string
    # start from the first position
    for end in range(1, len(s)): # O(n)  
      # if the char is in substring between the start and end index
      if s[end] in s[start:end]:
        # then calculate the result
        max_len = max(max_len, end - start) #
        index = s[start:end].index(s[end]) + len(s[:start])# 
        # set the start pointer
        start = index + 1

    # check for a string with no repeating characters
    # if the unique substring is towards the end
    max_len = max(max_len, len(s[start:end + 1]))
    
    # return the result
    return max_len
  
  # 5th attempt. O(n) time and O(1) space
  def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0:
      return 0
    
    if len(s) == 1:
      return 1
    # init two pointer
    start = 0 # O(1)
    end = 0 # O(1)
    # init a var to store the max length of substring
    max_substring = float("-inf") # O(1)
    
    # loop through the string
    while end < len(s): # O(n)
      # if current char is present in the string until now
      if s.find(s[end], start, end) != -1:
        # get the first index of the character
        index = s.find(s[end], start, end)
        # calculate the max length
        max_substring = max(max_substring, end - start)
        # increment the start pointer by 1
        start = index + 1
        
      # increment the end pointer
      end += 1
    
    # calculate the max among the max length and the length of substring
    max_substring = max(max_substring, len(s[start:end]))
    
    return max_substring
  
  # 6th attempt
  def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0:
      return 0
    
    if len(s) == 1:
      return 1
    
    # init two pointers
    start = 0 #1
    end = 0 #1
    # init a var to store the length
    max_len = 1 #1
    
    # loop through the string
    for end in range(1, len(s)): #1
      # check if any character before the end pointer matches the char at end pointer
      if s[end] in s[start:end]:
        # then calculate the length
        length = len(s[start:end]) 
        # calculate the max length so far
        max_len = max(max_len, length)
        # set the start pointer to the next index of matched char
        start =  s.index(s[end], start) + 1 
      else:
        # increment the end pointer
        end += 1  
        # increment the max length
        
      max_len = max(max_len, len(s[start:end]))
      
    # return the max length
    return max_len   
     
# 7th attempt
  def lengthOfLongestSubstring(self, s: str) -> int:
    start = 0
    end = 1
    
    substr_len = float('-inf')
    
    while end < len(s):
      if s[end] in s[start:end]:
        substr_len = max(substr_len, len(s[start:end]))
        start = s.index(s[end], start, end) + 1
      elif end == len(s) - 1:
          substr_len = max(substr_len, len(s[start:]))
          end += 1
      else:
        end += 1
    
    if substr_len == float('-inf'):
      return len(s)
    
    return substr_len
  
  # 8th attempt
  def lengthOfLongestSubstring(self, s: str) -> int:
    # is string has length 0
    start = 0
    end = 0
    max_len = 0

    while end < len(s):
      if s.find(s[end], start, end) != -1:
        max_len = max(max_len, len(s[start:end]))
        start = s.find(s[end], start, end) + 1
      end += 1
      
      max_len = max(max_len, len(s[start:end]))
    
    return max_len

  # Two pointer template
  if not s: return 0
        max_len = 0
        length = 0
        left = 0
        right = 0
        for right, rchar in enumerate(s):
            if s.find(rchar, left, right) != -1:
                left = s.find(rchar, left, right) + 1
            length = len(s[left: right + 1])
            max_len = max(max_len, length)
        return max_len
