# tc: o(b2*r), sc: o(b)
def apartmentHunting(blocks, reqs):
    max_distance_to_all_reqs_from_a_block = [float('-inf') for _ in range(len(blocks))] 

    for i in range(len(blocks)):
        for req in reqs:
            min_distance_to_a_req_from_a_block = float('inf')
            for j in range(len(blocks)):
                if req in blocks[j] and blocks[j][req]:
                    min_distance_to_a_req_from_a_block = min(min_distance_to_a_req_from_a_block, abs(j - i))

            max_distance_to_all_reqs_from_a_block[i] = max(max_distance_to_all_reqs_from_a_block[i], min_distance_to_a_req_from_a_block)
    
    min_val = min(max_distance_to_all_reqs_from_a_block)
    return max_distance_to_all_reqs_from_a_block.index(min_val)
