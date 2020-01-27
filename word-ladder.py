class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
  # init a new list
  list_words = []
  # init a list that will act as a Queue, the Queue will have the start word as the first element
  queue = [beginWord]
  # init a list to store all the alphabets
  alphabets = [chr(i) for i in range(ord('a'),ord('z')+1)]
  # init a var to store the transformations
  transformations = 0
  # loop through the word list
  for char in wordList:
    # insert the word in the list
    list_words.append(char)
  # if the list does not contains the end word
  if endWord not in list_words:  
    # then return 0
    return 0
    
  # loop until the queue is not empty
  while len(queue) != 0:
    # init a var to store the size of the Queue
    size = len(queue)
    # loop through the Queue
    for word in queue:
      # get the first element of the Queue
      
      # convert the string to a list of chars
      list_chars = list("word")
      # loop through the chars
      for index in range(len(list_chars)):
        # loop through the alphabet list
        for alphabet in alphabets
          # check if the char equals any char in the alphabet list
          if list_chars[index] == alphabet:
            # then continue
            continue
          # else if the char does not match the current char in the alphabet list
          else
            # then replace the char in the word with the current char in the alphabet list
            list_chars[index] = alphabet 
            # create a new word from the replaced char **Key step**. This step can help us check by transforming one character can we reach the next word in the list
            new_word = "".join(str(list_chars))
            # if the new word matches the end word
            if new_word == endWord:
              # then increment the transformation var
              transformation += 1
            # if the list contains the new word 
            if new_word in list_words:
              # then add it to the Queue
              queue.append(new_word)
              # remove it from the list because the transformation is already taken into account
              list_words.remove(new_word)
        # replace the replaced char with the original character; if this is not done then the character will have 'z' in it 
          list_chars[index] = word[index] #
      # increment the transformation var because the transformation was a success after changing one character
      # the success is guranteed because each character in the word is transformed and checked
      transformation += 1
