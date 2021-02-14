class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        
    def addWord(self, word: str) -> None:
        root = self.trie
        for char in word:
            if char not in root:
                root[char] = {}
            root = root[char]
        root['*'] = word

    def search(self, word: str) -> bool:
        root = self.trie
        return self._search(root, word)

    def _search(self, root, word):
        for i, char in enumerate(word):
            if char in root:
                root = root[char]
            else:
                if char == '.':
                    for key in root:
                        if key != '*' and self._search(root[key], word[i + 1:]):
                            return True
                    return False
                return False
        return '*' in root
