class Solution:
    def __init__(self):
        self.all_possible_abbreviations = []
        
    def generateAbbreviations(self, word: str) -> List[str]:
        self._generate_abbreviations(word, 0, 0, '')
        return self.all_possible_abbreviations
    
    def _generate_abbreviations(self, word, index, count, substring):
        if index == len(word) or count == len(word):
            self.all_possible_abbreviations.append(substring + (str(count) if count > 0 else ''))
            return
        self._generate_abbreviations(word, index + 1, count + 1, substring)
        self._generate_abbreviations(word, index + 1, 0, substring + (str(count) if count > 0 else '') + word[index])
        return
