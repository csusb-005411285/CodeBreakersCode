class Solution:
  # https://leetcode.com/problems/multiply-strings/discuss/17746/Python-easy-to-understand-solution-without-overflow-(with-comments).
  def multiply(self, num1: str, num2: str) -> str:
    # init a list to store the result
    # the list should have the length of num1 + num2
    result = [0] * (len(num1) + len(num2)) #
    
    carry = 0
    # loop through the first num
    for i in range(len(num2) -1, -1, -1):
      carry = 0
      # loop through the second num
      for j in range(len(num1) -1, -1, - 1):
        existing_value = result[i + j + 1]
        # calculate the product, the product should include the carry forward from the previous multiplication as well
        product = int(num2[i]) * int(num1[j]) + carry
        # calculate the carry. The existing value is from the previous multiplication. 
        # Carry is calculated by multiplication as well as addition, existing value 
        carry = (existing_value + product) // 10 
        # calculate the actual result value
        actual_product = (existing_value + product) % 10
        # append the actual result to the next index of the result
        result[i + j + 1] = actual_product
      # the carry on for the first element is appended to the start
      # += is for the addition
      result[i + j] += carry  # 
        
    result = "".join(map(str, result)) #
    if result.find("0") != -1:
      index = result.index("0")
      return result[index + 1:]
    else:
      return result
        
