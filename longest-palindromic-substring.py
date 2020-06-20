# 2nd attempt
def longestPalindromicSubstring(s: str):
    len_substr = 0
    substr = ''

    if len(s) == 1:
        return s

    for i in range(len(s) - 1):
        even_pal = get_even_palindrome(s, i, i + 1)
        odd_pal = get_odd_palindrome(s, i)

        result = [len(even_pal), even_pal] if len(even_pal) >= len(odd_pal) else [len(odd_pal), odd_pal]

        if result[0] > len_substr:
            len_substr = result[0] 
            substr = result[1] 

    return substr

# n, n
def get_odd_palindrome(s, i):
    back = i - 1
    forw = i + 1

    while back >= 0 and forw < len(s):
        if s[back] == s[forw]:
            back -= 1
            forw += 1
        else:
            break
    
    return s[back + 1: forw] 

# n, n
def get_even_palindrome(s, back, forw):
    while back >= 0 and forw < len(s):
        if s[back] == s[forw]:
            back -= 1
            forw += 1
        else:
            break
    
    return s[back + 1: forw]

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


