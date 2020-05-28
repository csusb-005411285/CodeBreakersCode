# tc: o(w * n log n), sc: o(wn)
def groupAnagrams(words):
	hash_map = {}

    for word in words:
        sorted_word = ''.join(sorted(word))

        if sorted_word not in hash_map:
            hash_map[sorted_word] = [word]
        else:
            hash_map[sorted_word].append(word)
        
    return hash_map.values()
