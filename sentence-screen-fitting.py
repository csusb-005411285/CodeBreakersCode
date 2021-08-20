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
                if word_len > cols:
                    return 0
                # if length of word > remaining cols
                if word_len > cols - col:
                    break
                # increment col by length of word
                col += word_len + 1
                # if index equals the last word of the sentence
                if idx == len(sentence) - 1:
                    # increment count
                    count += 1
                # increment index of sentence
                idx = (idx + 1) % len(sentence)
            # store in cache
            cache[start] = [count, idx]    
            # increment total
            num_times += count
        # return
        return num_times
