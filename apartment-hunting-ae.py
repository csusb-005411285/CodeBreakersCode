# tc: o(b2*r), sc: o(b)
def apartmentHunting(blocks, reqs):
    optimal_block = None
    max_distance_to_all_reqs_from_block = {}
    min_distance_to_all_reqs_from_all_block = float('inf')
    min_distance_to_a_req = float('inf')

    for i in range(len(blocks)):
        max_distance_to_all_reqs_from_block[i] = float('-inf')
        for j in range(len(reqs)):
            distance = 0
            min_distance_to_a_req = float('inf')
            for k in range(len(blocks)):
                if reqs[j] in blocks[k] and blocks[k][reqs[j]]:
                    distance = abs(k - i) 
                    min_distance_to_a_req = min(min_distance_to_a_req, distance)
            max_distance_to_all_reqs_from_block[i] = max(max_distance_to_all_reqs_from_block[i], min_distance_to_a_req)
    
        if min_distance_to_all_reqs_from_all_block > max_distance_to_all_reqs_from_block[i]:
            min_distance_to_all_reqs_from_all_block = max_distance_to_all_reqs_from_block[i]
            optimal_block = i
    return optimal_block
