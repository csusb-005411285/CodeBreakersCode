class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        start = end = 0
        while start < len(words):
            end = self.get_last_word_of_line(start, words, maxWidth)
            sentence = self.get_sentence(start, end, words, maxWidth)
            lines.append(sentence)
            start = end + 1
        return lines
    
    def get_last_word_of_line(self, start, words, max_width):
        end = start
        chars = 0
        while end < len(words) and chars + len(words[end]) + 1 <= max_width + 1:
            chars += len(words[end]) + 1
            end += 1
        return end - 1
    
    def get_sentence(self, start, end, words, max_width):
        line = []
        if start == end:
            return words[start] + self.generate_spaces(max_width - len(words[start]))
        total_chars = 0
        for i in range(start, end + 1):
            total_chars += len(words[i])
        last_line = True if end == len(words) - 1 else False
        spaces_that_can_be_added = max_width - total_chars
        equal_spaces = spaces_that_can_be_added // (end - start) if last_line is False else 1
        extra_spaces = spaces_that_can_be_added - equal_spaces * (end - start) if last_line is False else 0
        for i in range(start, end + 1):
            line.append(words[i])
            line.append(self.generate_spaces(equal_spaces))
            if extra_spaces:
                line.append(' ')
                extra_spaces -= 1
        sentence = ''.join(line[: -1]) # remove trailing white space. This is added after the last word.
        if not last_line:
            return sentence
        return sentence + self.generate_spaces(max_width - len(sentence)) #
    
    def generate_spaces(self, n):
        return ' ' * n;
