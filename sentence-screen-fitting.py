class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # init vars
        num_times = 0
        idx = 0
        cache = defaultdict(list)
        # check for invalid input
        
        # process
        # loop through rows
        for row in range(rows):
            start = idx
            count = 0
            col = 0
            # check if start index in cache
            if idx in cache:
                num, idx = cache[idx]
                num_times += num
                continue
            # loop through cols
            while col < cols:
                # get length of word
                word_len = len(sentence[idx])
                # if length of word > length of cols
                if word_len > cols: # 1
                    return 0
                # if length of word > remaining cols
                if word_len > cols - col: # 2
                    break
                # increment col by length of word
                col += word_len + 1 # 3
                # if index equals the last word of the sentence
                if idx == len(sentence) - 1:
                    # increment count
                    count += 1
                # increment index of sentence
                idx = (idx + 1) % len(sentence) # 4
            # store in cache
            cache[start] = [count, idx]    
            # increment total
            num_times += count
        # return
        return num_times
    
'''
1. If a sentence is longer than length of column
E.g 
["a", fooo"]
1
1

2. If the length of the current word is greater than the number of columns left.
3. Increase column by number of chars in the word + 1 for the space.
4. The index cannot go past the length of sentence.
'''
