class Solution:
    def __init__(self):
        self.valid = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        self.res = []
    
    def confusingNumberII(self, n: int) -> int:
        for key, val in self.valid.items(): # 1
            if key == 0:
                continue
            self.find_confusing_numbers(key, val, n, 1)
        return len(self.res)
    
    def find_confusing_numbers(self, n, rotate, _max, digit):
        if n > _max:
            return
        if n != rotate: # 4
            self.res.append(n) # 5
        digit = digit * 10 # 6
        for key, val in self.valid.items():
            num = n * 10 + key # 2
            num_rotated = self.valid[key] * digit + rotate # 3
            self.find_confusing_numbers(num, num_rotated, _max, digit)
        return

'''
1. Try to build a recursive tree with each confusing number as the root of the tree.
2. Append new digit to the existing number. When appending a new digit always use 10. Do not confuse
this with the digit argument from the function.
3. Rotate the new number. The first digit of the number should be value. For e.g {6 : 9} 
4. This condition satisfies the problem statement that the rotated number should not be same as the original number. 
5. Do not return after adding number to the final result set as this would always fail for {6: 9, 9: 6}   6. For every recursive call we make, the number of digits increase by 1. So we need to increase the
number of digits as this would be used to create the rotated number.
'''
