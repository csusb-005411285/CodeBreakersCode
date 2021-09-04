class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # init vars
        count = 0
        char_map = defaultdict(list)
        # build a map where the keys are the chars and the value is a list of indices
        for i, char in enumerate(s):
            char_map[char].append(i)
        # process
        # loop through words
        for word in words:
            # call helper method
            if self.is_substring(word, char_map):
                count += 1
        # return
        return count
    
    def is_substring(self, word, char_map):
        # init vars
        s_index = 0
        # loop through chars
        for i, char in enumerate(word):
            # if char not in map, return false
            if char not in char_map:
                return False
            # apply binary search
            index = bisect_left(char_map[char], s_index) # 1.
            # if index greater than the existing index, return False
            if index >= len(char_map[char]):
                return False
            # get the next index of the string
            s_index = char_map[char][index] + 1
        return True
    
'''
1. bisect_left finds is the index. It is always the existing index.
'''
