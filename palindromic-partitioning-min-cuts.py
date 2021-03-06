def palindromePartitioningMinCuts(string):
    # build the 2d matrix of palindromic substring
    is_pal = [[False for col in range(len(string))] for row in range(len(string))]
    # init a list to store min. cuts at the index
    cache = {i: i for i in range(len(string))}
    # build the 2d matrix
    for start_index in range(len(string)):
        for end_index in range(len(string)):
            is_pal[start_index][end_index] = is_palindrome(string[start_index: end_index + 1]) 

    # loop through the string
    for i in range(1, len(string)): # 2 o
        min_pal_len = float('inf')
        for j in range(0, i): # 1 o
            if is_pal[j][i]:
                if j == 0:
                    cache[i] = 0
                elif cache[j - 1] + 1 < min_pal_len: # 0 + 1 < i
                    min_pal_len = cache[j - 1] + 1 # 1
                    cache[i] = min(cache[i], min_pal_len)  # 1
            else:
                cache[i] = min(cache[i], cache[i - 1] + 1)
    return cache[len(string) - 1]

def is_palindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
