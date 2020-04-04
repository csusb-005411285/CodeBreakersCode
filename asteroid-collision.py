class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    if len(asteroids) == 0:
      return []
    
    if len(asteroids) == 1:
      return asteroids
    
    # init a var that will act as a stack
    stack = [] # O(n)
    # loop through the asteroids
    for ast in asteroids: # O(n)
      if ast < 0 and stack and stack[-1] > 0:
        append_to_stack = True
        while ast < 0 and stack and stack[-1] > 0: # O(n)
          if -ast > stack[-1]:
            stack.pop()
          elif ast == -stack[-1]:
            stack.pop()
            append_to_stack = False
            break
          else:
            append_to_stack = False
            break
        if append_to_stack:
          stack.append(ast)
      else:
        stack.append(ast)
    
    return stack
  
  # 2nd attempt
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    if len(asteroids) == 0:
      return []
    
    if len(asteroids) == 1:
      return asteroids
    
    stack = deque() #n
    stack.append(asteroids[0])
    
    for ast in asteroids[1:]: #n
      if stack and stack[-1] > 0:
        if ast > 0:
          stack.append(ast)
        else:
          if -ast < stack[-1]:
            continue
          if -ast == stack[-1]:
            stack.pop()
            continue
          while stack and -ast > stack[-1] and stack[-1] > 0: #n
            stack.pop()
          else:
            if stack and -ast == stack[-1]:
              stack.pop()
              continue
            if len(stack) == 0:
              stack.append(ast)
            else:
              if stack[-1] < 0:
                stack.append(ast)
      else:
        stack.append(ast)
        
    return stack
