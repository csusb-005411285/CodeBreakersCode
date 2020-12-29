# https://www.educative.io/courses/grokking-the-coding-interview/Y5YDWzqPn7O
def find_word_concatenation(str, words):
    result_indices = []
    word_map = Counter(words)
    for i in range(len(str) - len(words) * len(words[0]) + 1):
        word_found = defaultdict(int)
        num_words_found = 0
        for j in range(i, len(str), len(words[0])):
            new_word = str[j: j + len(words[0])]
            if new_word in word_map:
                word_found[new_word] += 1
                if word_found[new_word] == word_map[new_word]:
                    num_words_found += 1
                elif word_found[new_word] > word_map[new_word]: 
                    break
            else:
                break
        if num_words_found == len(word_map):
            result_indices.append(i)
    return result_indices
