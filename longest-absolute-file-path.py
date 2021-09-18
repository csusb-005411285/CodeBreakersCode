class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # init vars
        longest_absolute_path = 0
        stack = []
        # inital checks
        
        #process
        # split the string by \n
        paths = input.split("\n")
        # loop, process each word
        for path in paths:
            # split string by \t
            dir_files = path.split("\t")
            # calculate the depth of the word
            depth = len(dir_files) - 1 # 1
            # calculate length of the word
            word_len = len(dir_files[-1])
            # if the top of the stack has a depth equal to or greater than the current depth
            while stack and stack[-1][1] >= depth:
                # pop
                stack.pop()
            # if stack is empty
            if not stack:
                # add the length of string and the depth to the stack
                stack.append((word_len, 0))
            # if not
            else:
                # add to the stack
                # get the length from previous element
                prev_word_len = stack[-1][0] if stack else 0
                stack.append((prev_word_len + word_len, depth))
            # if word has '.'
            if '.' in dir_files[-1]:
                # calculate the max length
                longest_absolute_path = max(longest_absolute_path, stack[-1][0] + stack[-1][1])
        # return max length
        return longest_absolute_path
'''
1. dir\n\t has a depth of 0
'''
