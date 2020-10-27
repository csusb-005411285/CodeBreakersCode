class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        # use a cache to store values for repeated computations
        cache = OrderedDict()
        # use a helper method
        self.word_break_helper(s, 0, wordDict, cache)
        # return cache with key len(s)- 1
        pprint.pprint(cache)
        return list(cache.values())[-1]

    def word_break_helper(self, s, index, wordDict, cache): 
        # if index exists in cache
        if index in cache:
            return cache[index]
        # base case
        # when the index equals the length of string
        if index == len(s):
            return True
        is_found_in_dict = False
        # loop from index to end
        for i in range(len(s) - 1, index - 1, -1): 
            prefix = s[index: i + 1] 
            # if prefix in dict
            if prefix in wordDict: 
                pprint.pprint(prefix)
                # perfom recursion on suffix
                is_found_in_dict = self.word_break_helper(s, i + 1, wordDict, cache) 
                ## This is the key step. 
                # Return as soon as you find all the words in the suffix exist in the dict.
                if is_found_in_dict:
                    break
        # store value in cache, where index is the key and value is dependent on the returned value
        # of recursion
        cache[index] = is_found_in_dict 
        # return cache with key index 
        return cache[index] 
