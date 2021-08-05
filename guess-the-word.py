class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        # init vars
        i = 0
        matching_words = []
        match_value = 0
        # check for invalid inputs
        
        # perform steps
        while i < 11 and match_value != 6:
            word = random.choice(wordlist)
            match_value = master.guess(word)
            wordlist = self.find_matching_words(word, wordlist, match_value)
            i += 1
        return word
    
    def find_matching_words(self, word, words, val):
        matching_words = []
        for w in words:
            count = 0
            for char1, char2 in zip(w, word):
                if char1 == char2:
                    count += 1
            if count == val:
                matching_words.append(w)
        return matching_words
