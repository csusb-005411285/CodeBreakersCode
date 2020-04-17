# 3rd attempt
from collections import deque

class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    # init a deck
    stack = deque() #n
    # loop through the list
    for ast in asteroids: #n  
      # if the top of the stack is positive and the incoming ast is negative
      while stack and stack[-1] > 0 and ast < 0: #n
        # then check if the incoming is greater 
        if -ast > stack[-1]:
          # then pop the element from the top of the stack
          stack.pop()
        # if the top of the stack and the incoming element is equal
        elif -ast == stack[-1]:
          stack.pop()
          break 
        else:
          break 
      else:
        stack.append(ast)
        
    return stack 
  
  # 5th attempt
  def asteroidCollision(self, asteroids: [int]) -> [int]:
    stack = deque()

    for ast in asteroids:
      if stack and stack[-1] > 0 and ast < 0:
        while stack and stack[-1] > 0 and -ast > stack[-1]:
          stack.pop()
          
        if not stack:
          stack.append(ast)
          continue
          
        if -ast == stack[-1]:
          stack.pop()
          continue
          
        if -ast > stack[-1]:
          stack.append(ast)
      else:
        stack.append(ast)
    
    return list(stack)
