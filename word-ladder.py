class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        if not beginWord or not endWord or not wordList:
            return 0

        queue = deque()
        visited = {}
        words_map = self.generate_words_map(wordList) 
        queue.append([beginWord, 1]) # 
        visited[beginWord] = True
    
        while queue:
            word, step = queue.popleft()

            if word in visited and visited[word]: #
                continue

            if word == endWord:
                return step 
            
            visited[word] = True
            neighbors = self.get_neighbors(word) #

            for neighbor in neighbors:
                if neighbor in words_map:
                    for neigh_word in words_map[neighbor]:
                        queue.append([neigh_word, step + 1])
        
        return 0

    def get_neighbors(self, word):
        all_possible_words = []
    
        for i in range(len(word)):
            new_word = word[:i] + '*' + word[i + 1:] 
            all_possible_words.append(new_word)
        
        return all_possible_words
    
    def generate_words_map(self, wordList):
        word_map = {}
    
        for i in range(len(wordList)):
            word = wordList[i]
            new_word = '' 

            for c in range(len(word)):
                new_word = word[:c] + '*' + word[c + 1:]
    
                if new_word not in word_map:
                    word_map[new_word] = [word]
                else:
                    word_map[new_word].append(word)
    
        return word_map
