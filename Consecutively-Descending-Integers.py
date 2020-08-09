class Solution:
    def solve(self, s):
        # init a var is_descending
        is_desc = False
        
        # loop through the string. start from the end
        for i in range(len(s) - 1, 0, -1):    
            # call the helper dfs method
            is_desc = self.solve_helper(i, len(s), s) # 7 
            
            # if the helper method returns ture:
            if is_desc:    
                return True
                
        return False
    
    def solve_helper(self, char_index, char_index_end, s):
        if char_index <= 0:
            return True
        
        # 1 0 0 9 9 9 8 9 7
        # 0 1 2 3 4 5 6 7 8
        # convert the string pointed by char_index to int
        curr_int = int(s[char_index: char_index_end]) # s[3: 5] 99
        # calculate the next integer
        expected_next_int = curr_int + 1 # 100
        # calculate the size of next integer
        expected_next_int_size = len(str(expected_next_int)) # 3
        # calculate the start index of next integer
        expected_next_int_index = char_index - expected_next_int_size # 3 - 3 = 0
        # get the next integer
        actual_next_int = 0
        if expected_next_int_index >= 0:
            actual_next_int = int(s[expected_next_int_index: char_index]) # s[0: 3] 100
        
        res = False
        # if the current integer + 1 equals next integer:
        if curr_int + 1 == actual_next_int: # 99 + 1 == 100
            # recursively call the dfs method
            print(expected_next_int_index)
            res = self.solve_helper(expected_next_int_index, char_index, s) # 0, 3
            
            if res:
                return True
            
        return False
        
