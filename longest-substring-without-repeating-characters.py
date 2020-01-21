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
      
        
