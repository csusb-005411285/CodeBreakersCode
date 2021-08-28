# Top-down
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # init vars
        len_longest_word_chain = 0
        cache = defaultdict(int)
        # initial checks
        # sort words
        words.sort(key = lambda x: -len(x))
        # loop through all the words
        for word in words:
            # perform dfs
            len_longest_word_chain = max(len_longest_word_chain, self.longest_str_chain(word, words, cache) + 1) # 1.
        # return
        return len_longest_word_chain if len_longest_word_chain != 0 else 1 # 2.
    
    def longest_str_chain(self, word, words, cache):
        if word in cache:
            return cache[word]
        # base case
        _max = 0
        # loop through each char in the word
        for i, char in enumerate(word):
            # remove the char from word
            new_word = word[:i] + word[i + 1:]
            # if word is in the list of words
            if new_word in words:
                # perform dfs
                _max = max(_max, self.longest_str_chain(new_word, words, cache) + 1)
                # get max value
        # return max value
        cache[word] = _max
        return _max
    
'''
1. +1 is for the base case.
2. smallest word chain can be of length 1.
'''

# Bottom-up
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # init vars
        cache = defaultdict(int)
        for word in words:
            cache[word] = 1
        longest_chain_len = 0
        # initial checks
        if len(words) == 1:
            return 1
        words.sort(key = lambda x: len(x))
        # process
        for word in words:
            for i, char in enumerate(word):
                new_word = word[:i] + word[i + 1:]
                # check if the char is present in the cache
                if new_word in cache:
                    cache[word] = max(cache[word], cache[new_word] + 1)
                    longest_chain_len = max(longest_chain_len, cache[word])
            # if present store the max value in the cache
        # return
        return longest_chain_len if longest_chain_len != 0 else 1

def longestStringChain(strings):
    if not strings:
        return []
    # init a hash table
    cache = {}
    # populate the cache 
    for s in strings:
        cache[s] = ('', 1)
    # sort the string
    strings.sort(key=lambda x: len(x))

    # loop through the string
    for s in strings:
        # use helper method to find the longest chain
        find_longest_chain(s, cache)
        
    # build the string chain
    return build_string_chain(cache)

def find_longest_chain(s, cache):
    # iterate through the chars of a string
    for i in range(len(s)):
        # use helper method to get substring
        new_str = s[:i] + s[i + 1:]
        # check if string in cache
        # if string in chain
        if new_str in cache:
            # update cache
            if cache[new_str][1] + 1 > cache[s][1]:
                cache[s] = (new_str, cache[new_str][1] + 1)  

def build_string_chain(cache):
    max_val = 0
    start_str = ''
    seq = []
    # get the key of the string with maximum number of chains
    for k, tup in cache.items():
        if tup[1] >= max_val:
            max_val = tup[1] 
            start_str = k
    # append the key to the result
    seq.append(start_str)
    curr = start_str
    # loop through the cache
    # loop until the next string in the chain is not empty
    while curr in cache and cache[curr][0]: #man
        # keep adding strings to the result
        seq.append(cache[curr][0])
        curr = cache[curr][0]

    return seq if len(seq) > 1 else []
