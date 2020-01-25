def longestSubstringWithoutDuplication(string):
    # Write your code here.
	if len(string) <= 1:
		return string
	# init a left pointer
	left = 0
	# init a dictionary
	char_index = {}
	# init a susbstring variable to store the result
	substring = ''
	curr_substring = ''
	char = ''
	# loop through the string
	for right in range(0, len(string)):
		char = string[right]
		# if the char exisits in the dictionary
		if char in char_index:
			# get the index and chose the index next to it as the left pointer
			duplicate_char_index = char_index[char]
			# but, if the index is less than the left pointer's current position
			# choose the max value of index and the left pointer's position
			left = max(left, duplicate_char_index + 1)
			curr_substring = ''
		# for each char store it in the dictionary along with its index
		char_index[char] = right	
		# append the string to substring variable
		curr_substring = string[left:right + 1]
		# also check if the string to append is has a greater length than the existing length
		substring = substring if len(substring) >  len(curr_substring) else curr_substring 
	# return the substring
	return substring	
				
    pass
