class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # init vars
        val = 0
        bin_val_len = 0
        # inital checks
        
        # process
        # loop
        for i in range(1, n + 1):
            # find binary val of num
            if (i & (i - 1)) == 0:
                # find length of num
                bin_val_len += 1
                # move val by length bits to the left
            # use <<
            val = val << bin_val_len
            # concatenate val and binary val
            val = (val | i) % (pow(10, 9) + 7)
        # return
        return val 
