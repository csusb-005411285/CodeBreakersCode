class Solution:
  def lemonadeChange(self, bills: List[int]) -> bool:
    if len(bills) == 0:
      return True
    # initialize two vars, one to store the fives and the other to store the tens
    fives, tens = 0, 0
    # loop through the list
    for i in range(len(bills)):  
      # if bill is 5
      if bills[i] == 5:  
        # increment var five
        fives += 1
      # if bill is 10
      elif bills[i]  == 10:  
        # increment 10
        tens += 1
        # decrement 5
        fives -= 1
      # if bill is 20
      elif bills[i]  == 20:  
        # if 10 > 0
        if tens > 0:  
          # decrement 10
          tens -= 1
          # decrement 5
          fives -= 1
        # else
        else:  
          # decrement 5 by 3
          fives -= 3
      
      # if 5 is less than 0
      if fives < 0:
        return False

    return True
  
