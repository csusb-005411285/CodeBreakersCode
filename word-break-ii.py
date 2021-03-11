class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = defaultdict(list)
        self._word_break(s, wordDict, cache, 0)
        return cache[0]
    
    def _word_break(self, s, words, cache, index):
        if index in cache:
            return cache[index]
        if index >= len(s):
            return ['']
        for i, word in enumerate(words):
            if s[index: index + len(word)] == word:
                for segment in self._word_break(s, words, cache, index + len(word)):
                    new_word = word + ' ' + segment if segment != '' else word
                    cache[index].append(new_word)
        if index not in cache:
            cache[index] = []
        return cache[index]
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = defaultdict(list)
        self._word_break(s, wordDict, cache)
        return cache[s]
    
    def _word_break(self, s, words, cache):
        if s in cache:
            return cache[s]
        if not s:
            return ['']
        for word in words:
            if s.startswith(word):
                prefix = s[:len(word)]
                suffix = s[len(word):]
                for result in self._word_break(suffix, words, cache):
                    cache[s].append(prefix + ' ' + result if result else prefix)
        return cache[s]
