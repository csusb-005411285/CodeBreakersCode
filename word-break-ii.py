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
