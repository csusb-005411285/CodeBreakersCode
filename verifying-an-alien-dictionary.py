class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = defaultdict(int)
        is_equal = True
        for i, char in enumerate(order):
            order_map[char] = i
        for i in range(len(words) - 1):
            is_equal = self.compare_words(words[i], words[i + 1], order_map)
            if not is_equal:
                return False
        return True

    def compare_words(self, word1, word2, order_map):
        combined_words = zip(word1, word2)
        for char1, char2 in combined_words:
            if order_map[char1] < order_map[char2]:
                return True
            elif order_map[char1] > order_map[char2]:
                return False
        return True if len(word1) <= len(word2) else False
