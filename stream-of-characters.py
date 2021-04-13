class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = defaultdict(dict)
        self.queue = deque([])
        for i, word in enumerate(words):
            trie = self.trie
            for j, char in enumerate(word[::-1]):
                if char not in trie:
                    trie[char] = {}
                trie = trie[char]
            trie['*'] = word

    def query(self, letter: str) -> bool:
        self.queue.appendleft(letter)
        trie = self.trie
        for i, char in enumerate(self.queue):
            if '*' in trie:
                return True
            elif char in trie:
                trie = trie[char]
            elif char not in trie:
                return False
        return '*' in trie
                
