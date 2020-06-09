def smallestSubstringContaining(bigString, smallString):
	target_char_counts = count_chars(smallString)
	substring_index = find_smalllest_substring_index(target_char_counts, bigString)
	return substring_index

def find_smalllest_substring_index(original_chars_map, s):
	front = 0 
	back = 0
	unique_chars = 0
	unique_chars_map = {}
	actual_unique_chars_len = len(original_chars_map.keys())
	smallest_substr = ''
	smallest_substr_len = float('inf')

	while front < len(s):
		front_char = s[front]

		if front_char not in original_chars_map:
			front += 1
			continue

		if front_char not in unique_chars_map:
			unique_chars_map[front_char] = 0

		unique_chars_map[front_char] += 1

		if unique_chars_map[front_char] == original_chars_map[front_char]:
			unique_chars += 1
				
		while unique_chars == actual_unique_chars_len:
			substr = s[back: front + 1]

			if len(substr) <= smallest_substr_len :
				smallest_substr = substr
				smallest_substr_len = len(substr)
			
			if s[back] not in original_chars_map:
				back += 1
				continue

			if unique_chars_map[s[back]] == original_chars_map[s[back]]:
				unique_chars -= 1

			unique_chars_map[s[back]] -= 1
			back += 1

		front += 1

	return smallest_substr 
		
def count_chars(smallString):
	char_map = {}

	for c in smallString:
		increase_char_count(c, char_map)
	
	return char_map

def increase_char_count(c, char_map):
		if c not in char_map:
			char_map[c] = 0
		
		char_map[c] += 1
 
