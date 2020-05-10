# tc: o(n2), sc: o(1)
def longestPalindromicSubstring(string):
    if len(string) == 1:
        return string
        
    largest_substring_len = 0
    largest_substring = ''
    largest_substring_len_curr_index = 0
    largest_substring_curr_index = 0

    for i in range(1, len(string)):
        even_length_substring = get_palindrome(string, i-1, i)
        odd_length_substring = get_palindrome(string, i-1, i+1)

        if len(even_length_substring) <= len(odd_length_substring):
            largest_substring_curr_index = odd_length_substring
            largest_substring_len_curr_index = len(odd_length_substring)
        else:
            largest_substring_curr_index = even_length_substring
            largest_substring_len_curr_index = len(even_length_substring)

        if largest_substring_len < largest_substring_len_curr_index:
            largest_substring_len = largest_substring_len_curr_index 
            largest_substring = largest_substring_curr_index

    return largest_substring

def get_palindrome(string, start_index, end_index):
    curr_start_index = 0 
    curr_end_index = 0 
    while start_index >= 0 and end_index < len(string):
        if string[start_index] == string[end_index]:
            curr_start_index = start_index
            curr_end_index = end_index
            start_index -= 1
            end_index += 1
        else:
            break
    return string[curr_start_index: curr_end_index+1]
