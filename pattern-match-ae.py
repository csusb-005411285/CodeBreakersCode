def patternMatcher(pattern, string):
    pattern_switched = False

    if pattern[0] == 'y':
        pattern = reverse_pattern(pattern)
        pattern_switched = True

    pattern_map = {}
    get_pattern_count(pattern, pattern_map)
    word_len = get_word_len_matching_pattern(pattern, string, pattern_map)

    for i in range(1, len(string)):
        str_x = get_str_x(i, string, pattern_map)
        str_y = ''

        if 'y' in pattern_map:
            str_y = get_str_y(i, string, pattern_map, pattern)

        matched_string = does_match_pattern(str_x, str_y, string, pattern)

        if matched_string:
            if not pattern_switched:
                return matched_string
            else:
                return list(reversed(matched_string))

    return [] 

def reverse_pattern(pattern):
    result = ''

    for i in pattern:
        if i == 'y':
            result += 'x'
        else:
            result += 'y'

    return result

def does_match_pattern(s1, s2, string, pattern):
    result = ''

    for p in pattern:
        if p == 'x':
            result += s1
        else:
            result += s2

    if result == string:
        return [s1, s2]

    return [] 

def get_str_y(i, s, pattern_map, pattern):
    num_xs = pattern_map['x']
    num_ys = pattern_map['y']
    len_y = (len(s) - (i * num_xs))//num_ys
    start_index = i * pattern.index('y') 

    return s[start_index: start_index + len_y]

def get_str_x(i, s, pattern_map):
    return s[0: i]

def get_word_len_matching_pattern(pattern, string, pattern_match):
    results = []
    
    for i in range(1, len(string)):
        x_len = pattern_match['x'] * i

        if 'y' not in pattern_match:
            results.append([i])

        elif ((len(string) - x_len) % pattern_match['y']) == 0 and (len(string) - x_len) > 0:
            y_len = (len(string) - x_len) // pattern_match['y']
            results.append([i, y_len])
    
    return results

def get_pattern_count(pattern, pattern_map):
    for p in pattern:
        if p in pattern_map:
            pattern_map[p] += 1
        else:
            pattern_map[p] = 1
