def longestStringChain(strings):
    if not strings:
        return []
    # init a hash table
    cache = {}
    # populate the cache 
    for s in strings:
        cache[s] = ('', 1)
    # sort the string
    strings.sort(key=lambda x: len(x))

    # loop through the string
    for s in strings:
        # use helper method to find the longest chain
        find_longest_chain(s, cache)
        
    # build the string chain
    return build_string_chain(cache)

def find_longest_chain(s, cache):
    # iterate through the chars of a string
    for i in range(len(s)):
        # use helper method to get substring
        new_str = s[:i] + s[i + 1:]
        # check if string in cache
        # if string in chain
        if new_str in cache:
            # update cache
            if cache[new_str][1] + 1 > cache[s][1]:
                cache[s] = (new_str, cache[new_str][1] + 1)  

def build_string_chain(cache):
    max_val = 0
    start_str = ''
    seq = []
    # get the key of the string with maximum number of chains
    for k, tup in cache.items():
        if tup[1] >= max_val:
            max_val = tup[1] 
            start_str = k
    # append the key to the result
    seq.append(start_str)
    curr = start_str
    # loop through the cache
    # loop until the next string in the chain is not empty
    while curr in cache and cache[curr][0]: #man
        # keep adding strings to the result
        seq.append(cache[curr][0])
        curr = cache[curr][0]

    return seq if len(seq) > 1 else []
