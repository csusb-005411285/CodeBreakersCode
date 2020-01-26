def underscorifySubstring(string, substring):
    # Write your code here.
	locations = collapse(find_location_substring(string, substring))
	return underscore_words(locations, string)

def find_location_substring(string, substring):
	# initalize a list to store the start and end index of the substring
	substr_locations = []
	curr = 0
	# loop through the string
	while curr < len(string):	
		# use the find function to get the start index of the string
		if string.find(substring, curr) != -1:
			index = string.find(substring, curr)
			# store the start and end index in the list
			substr_locations.append([index, index + len(substring)])
			curr = index + 1
		else:
			break
	# return a list that contains the start and end indexes of the substring in the string
	return substr_locations

def collapse(substr_list):
	if len(substr_list) <= 1:
		return substr_list
	# init a list to store the start and end index
	non_overlapping_substr = []
	curr = 1
	prev = 0
	non_overlapping_substr.append(substr_list[0])
	# loop through the list
	while curr < len(substr_list):
		# check if the previous ending index is greater than current starting index
		if substr_list[prev][1] >= substr_list[curr][0]:
			# then set the previous last index to the current last index
			substr_list[prev][1] = substr_list[curr][1]
		else:	
			# store the current list in the list to be returned
			non_overlapping_substr.append(substr_list[curr])
			prev = curr
		curr += 1
	# return the list
	return non_overlapping_substr

def underscore_words(str_list, string):
	# initialize a pointer to keep track of string index and index of the list
	str_index = 0
	# init a var to store the result
	underscore_str = ''
	# init a var to keep track of 0th or 1st index
	index = 0
	# init a var to keep track of elements in the list
	list_index = 0
	# loop through the list and string together
	while str_index < len(string) and list_index < len(str_list):
		# if the current index of the string matches index of the element of the list, check for the 0th index first
		if str_index == str_list[list_index][index]:
			# then append an underscore to the result var
			underscore_str += "_"
			# if index if 1 
			if index == 1:
				# then increment to the next element in the list
				list_index += 1
			# change the index to 1 if it was 0 or vice versa
			index = 0 if index == 1 else 1
		# append the char to result var
		underscore_str += string[str_index]
		# increment the curr pointer
		str_index += 1
	# if curr pointer did not reach the end of the string, but the end of the list is reached
	if str_index < len(string):
		# then append the remaining chars to the result
		underscore_str += string[str_index:]
	if list_index < len(str_list):
		underscore_str += '_'
	
	return underscore_str

