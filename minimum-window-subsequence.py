class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        # init vars
        # two pointers
        s1ptr = s2ptr = 0
        # store string length
        str_len = float('inf')
        # store final string
        min_substring = ''
        # inital checks
        # check if s1 or s2 has a length of 0
        if not s1 or not s2:
            return 0
        # process
        # outer while loop until the end of s1
        while s1ptr < len(s1):
            right = s1ptr
            # inner while loop to loop until the end of s1
            while right < len(s1):
                # if chars are equal
                if s1[right] == s2[s2ptr]:
                    # increment s2 pointers
                    s2ptr += 1
                # if we reach end of s2
                if s2ptr == len(s2):
                    break
                # increment s1 pointer
                right += 1
            # if we are at the end of s1
            if right == len(s1):
                break
            # optimization step
            # set left to right
            left = right
            # set another pointer to last index of s2
            # traverse backwards
            s2ptr -=1
            while s2ptr >= 0: # 2.
                # compare with chars of s2
                # if chars are equal move backward
                #print(left, s2ptr)
                if s1[left] == s2[s2ptr]:
                    s2ptr -= 1
                # if we go beyond 0
                if s2ptr < 0:
                    break
                # move left back
                left -= 1 # 3.
            # compare lengths
            if str_len > right - left + 1:    
                # store min lenght
                str_len = right - left + 1
                # store min substring
                min_substring = s1[left : right + 1]
            # set the s1 ptr to point to next index of s2 ptr
            s1ptr = left + 1 # 1. 
        # return min string
        return "" if s1ptr == 0 and s2ptr == 0 else min_substring
        
'''
1. When we are here s2ptr = 0. We do not start s1ptr from right + 1. As right + 1 is the longest subsequence containing all characters of s2.
2. The condition should be >= 0 and not while s2ptr:
3. left can point to chars in s2 and chars not in s2.
'''
