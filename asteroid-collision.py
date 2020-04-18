# 3rd attempt
from collections import deque

class Solution:

  # 6th attempt
  def asteroidCollision(self, asteroids: [int]) -> [int]:
    stack = deque()

    for i in range(len(asteroids)):
      if stack and stack[-1] > 0 and asteroids[i] < 0:
        while stack and -asteroids[i] > stack[-1] and stack[-1] > 0:
          stack.pop()
         
        if not stack:
          stack.append(asteroids[i])
          continue
          
        if stack[-1] < 0:
          stack.append(asteroids[i])
          continue

        if -asteroids[i] == stack[-1]:
          stack.pop()
          continue
      else:
        stack.append(asteroids[i])
    return list(stack)
