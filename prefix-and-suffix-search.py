class WordFilter:

    def __init__(self, words: List[str]):
        # init vars
        # prefix dict
        self.prefix_map = defaultdict(set)
        # suffix dict
        self.suffix_map = defaultdict(set)
        # weight dict
        self.weights_map = defaultdict(int)
        # loop through the words
        for i, word in enumerate(words):
            # init vars to store prefix and suffix
            prefix = ''
            suffix = ''
            # store prefixes
            # loop through char of each word
            # start the word with an empty char
            for char in [''] + list(word):
                # build the prefix
                prefix += char
                # add to dict
                self.prefix_map[prefix].add(word)
            # store suffixes
            # loop through char of each word
            # reverse the word before looping
            for char in [''] + list(word[::-1]):
                # build the suffix
                suffix += char
                # add to dict
                # when adding to the dict, reverse the suffix
                self.suffix_map[suffix[::-1]].add(word)
            # store the word and its index in a separate dict
            self.weights_map[word] = i

    def f(self, prefix: str, suffix: str) -> int:
        # init a var to store the common words
        common_words = []
        # init a var to store the index
        max_index = -1
        # if the prefix and suffix exists in the dict
        if prefix in self.prefix_map and suffix in self.suffix_map:    
            # check if each word in the prefix exist in the suffix
            for word in self.prefix_map[prefix]:
                # store the common words in a var
                if word in self.suffix_map[suffix]:
                    common_words.append(word)
        # loop through the list of words found
        for word in common_words:
            # store the max index
            max_index = max(max_index, self.weights_map[word])
        # return the max index
        return max_index
    
