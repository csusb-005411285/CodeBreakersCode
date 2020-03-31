def get_permutations(string):
    if len(string) == 0:
        return {''} 
    # Generate all permutations of the input string
    if len(string) == 1:
        return {string}

    str_len = len(string)
    last_char = string[str_len - 1:]
    all_chars_except_last = string[:str_len - 1]
    
    permutations = get_permutations(all_chars_except_last)
    results = set()
    for permutation in permutations:
        for char in range(len(permutation) + 1):
            results.add(permutation[:char] + last_char + permutation[char:])

    return results 
