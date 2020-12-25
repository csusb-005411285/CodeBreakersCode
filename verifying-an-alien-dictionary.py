class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_map = defaultdict(int)
        for i, char in enumerate(order):
            char_map[char] = i
        is_sorted = True
        for i in range(len(words) - 1):
            if words[i] == words[i + 1]: return True
            curr_word = self.get_word_order(words[i], char_map) 
            next_word = self.get_word_order(words[i + 1], char_map) 
            is_sorted = self.compare_words(curr_word, next_word)
            if not is_sorted: return False
        return True

    def compare_words(self, word1, word2):
        words_combine = list(zip(word1, word2))
        for i, word in enumerate(words_combine):
            if word[0] < word[1]:
                return True 
            elif word[0] > word[1]:
                return False
        return True if len(word1) < len(word2) else False

    def get_word_order(self, word, char_map):
        word_order = []
        for i, char in enumerate(word):
            word_order.append(char_map[char])
        return word_order 
