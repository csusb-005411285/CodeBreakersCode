class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
      if (tokens is None):
        return -1
      #initalize two variables to store the elments during division and substraction
      first_operand = 0
      second_operand = 0
      #initialize a list which would act as a Stack
      stack = []
      # loop through all the tokens
      for token in tokens:
        # if we encounter any operator then pop the two recent elements and perform operations on them
        # push them back into the stack
        if (token == '+') :
          first_operand = int(stack.pop())
          second_operand = int(stack.pop())
          stack.append(first_operand + second_operand)
        elif (token == '-'):
          second_operand = int(stack.pop())
          first_operand = int(stack.pop())
          stack.append(first_operand - second_operand)
        elif (token == '/'):
          second_operand = int(stack.pop())
          first_operand = int(stack.pop())
          stack.append(int(first_operand / second_operand))
        elif (token == '*'):
          first_operand = int(stack.pop())
          second_operand = int(stack.pop())
          stack.append(first_operand * second_operand)
        else:
          # for each token push them into the list
          stack.append(token)
        

      
      # return the only element in the stack
      return stack.pop()
        
