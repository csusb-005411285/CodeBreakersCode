def longestPalindromicSubstring(string):
    # Write your code here.
	# init a list to store the start and end index
	palindrome_index = [0, 1]	
	# loop through the string
	for char in range(1, len(string)):
		# for every char, check if it is a part of Palindrome substring
		# check for even palindrome
		odd = getPalindromeIndex(string, char - 1, char + 1)
		even = getPalindromeIndex(string, char - 1, char)
		# check for odd palindrome
		max_so_far = max(odd, even, key = lambda x: x[1] - x[0])
		# store the max of even and odd palindrome
		palindrome_index = max(palindrome_index, max_so_far, key = lambda x: x[1] - x[0])
		# store the start and end index of max palindrome so far
	return string[palindrome_index[0]:palindrome_index[1]]

def getPalindromeIndex(string, left_index, right_index):
	while left_index >= 0  and right_index < len(string):
		if string[left_index] != string[right_index]:
			break
		left_index -= 1
		right_index += 1
	return [left_index + 1, right_index]


