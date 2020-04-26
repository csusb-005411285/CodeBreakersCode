# tc: o(n2), sc: o(n)
def rectangleMania(coords):
    coord_map = {}
    num_rectangles = 0
    for coord in coords:
        coord_key = generate_key(coord)
        coord_map[coord_key] = generate_coord_map(coords, coord)
    
    for vertex in coords:
        num_rectangles += rectangle_mania_helper(coords, vertex, coord_map, vertex, 'up', 0)
    
    return num_rectangles

def generate_coord_map(coords, origin):
    coord_dict = {
        'left': [],
        'right': [],
        'up': [],
        'down': [],
    }
    x, y = origin
    for coord in coords:
        if coord[1] == y and coord[0] < x:
            coord_dict['left'].append([coord[0], coord[1]]) 
        elif coord[1] == y and coord[0] > x:
            coord_dict['right'].append([coord[0], coord[1]]) 
        elif coord[0] == x and coord[1] > y:
            coord_dict['up'].append([coord[0], coord[1]]) 
        elif coord[0] == x and coord[1] < y:
            coord_dict['down'].append([coord[0], coord[1]]) 
    return coord_dict

# tc: o(v + e)
def rectangle_mania_helper(coords, vertex, coord_table, origin, direction = 'up', num_rect = 0):
    coord_key = generate_key(vertex)
    if direction == 'left':
        if origin in coord_table[coord_key]['left']:
            return 1
        else:
            return 0

    next_direction = get_next_direction(direction)
    for neighbor in coord_table[coord_key][direction]: 
        num_rect += rectangle_mania_helper(coords, neighbor, coord_table ,origin, next_direction, 0)

    return num_rect 

def get_next_direction(curr_direction):
    if curr_direction == 'up':
        return 'right'
    if curr_direction == 'right':
        return 'down'
    if curr_direction == 'down':
        return 'left'
    return 'up'

def generate_key(coord):
    return str(coord[0]) + ', ' + str(coord[1])
