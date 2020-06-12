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

# 2nd approach
# tc: o(n), sc: o(n)
def apartmentHunting(blocks, reqs):
    distances = {}
    max_distances_from_each_block = get_max_distances_from_each_block(blocks, reqs, distances)
    max_distance_to_all_reqs_from_a_block = get_max_distances_to_reqs(list(zip(*list(max_distances_from_each_block.values()))))
    min_val = min(max_distance_to_all_reqs_from_a_block)
    return max_distance_to_all_reqs_from_a_block.index(min_val)

def get_max_distances_to_reqs(distance):
    result = []

    for i in range(len(distance)):
        result.append(max(distance[i])) 

    return result


def get_max_distances_from_each_block(blocks, reqs, distances):
    for req in reqs:
        distances[req] = [float('inf') for row in blocks]
        
        #forward sweep
        for i in range(len(blocks)):
            if blocks[i][req]:
                distances[req][i] = 0
            else:
                if i == 0:
                    distances[req][i] = min(float('inf'), distances[req][i])
                else:
                    distances[req][i] = min(distances[req][i], distances[req][i - 1] + 1)
        
        # backward sweep
        for j in range(len(blocks) - 1, -1, -1):
            if blocks[j][req]:
                distances[req][j] = 0
            else:
                if j == len(blocks) - 1:
                    distances[req][j] = min(float('inf'), distances[req][j])
                else:
                    distances[req][j] = min(distances[req][j], distances[req][j + 1] + 1)
        
    return distances
