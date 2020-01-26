def groupAnagrams(words):
    # Write your code here.
	# init a hashmap
	if len(words) == 0:
		return []
	if len(words) == 1:
		return [words]
	
	hashmap = {} #
	word = 0
	sorted_word = ''
	# loop through the list
	for word in words:
		# sort each word by its character
		sorted_word = "".join(sorted(word))
		# if the word exists in the list
		if sorted_word in hashmap:
			# find the index and append the word to the list in that index
			hashmap[sorted_word].append(word)
		# else
		else:
			# insert a new list with the sorted word as the key and original word
			# as the value
			hashmap[sorted_word] = [word] #
		
	# return the values of the hashmap
	return hashmap.values()
