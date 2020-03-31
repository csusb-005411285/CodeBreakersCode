def get_closing_paren(sentence, opening_paren_index):
    # init a var to store the count
    count = 0 # O(1)
    # loop through the sentence
    for pos in range(opening_paren_index, len(sentence)): # O(n)
        # if the char is an opening brace
        if sentence[pos] == '(':
            # increment the count
            count += 1
        
        # if the char is a closing brace
        elif sentence[pos] == ')': 
            # decrement the count
            count -= 1
            
            # if count is 0
            if count == 0:
                # then return the position
                return pos
        # else
        else:
            # continue
            continue
        
    raise Exception()
