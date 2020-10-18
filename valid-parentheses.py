# https://www.interviewcake.com/question/python3/bracket-validator?course=fc1&section=queues-stacks
def is_valid(code):
    # Determine if the input code is valid
    #init a stack n
    stack = deque()
    hash_map = {}
    hash_map['}'] = '{'
    hash_map[']'] = '['
    hash_map[')'] = '('

    # loop through the string
    # ()
    for char in code: # (
        # if the char is an opening brace
        if char in hash_map.values():
            # place it in the stack
            stack.append(char) # [(]
        # if the char is a closing brace
        elif char in hash_map.keys(): # )
            # before popping check if an element exists in the stack
            if stack:
                prev_char = stack.pop() # (
            else:
                return False
            # if the popped element does not match the incoming element
            if hash_map[char] != prev_char: # ) != ( 
                return False
    
    return True if not stack else False 
