# tc: o(n), sc: o(n)
def zigzagTraverse(array):
	results = []
    direction = 'down'
    row = 0
    col = 0

    while is_valid_cell(array, row, col):
        if direction == 'down':
            if row == len(array) - 1 and col == 0:
                results.append(array[row][col])
                col += 1
                direction = 'up'
            elif row == len(array) - 1:
                results.append(array[row][col])
                col += 1
                direction = 'up'
            elif col == 0:
                results.append(array[row][col])
                row += 1
                direction = 'up'
            else:
                results.append(array[row][col])
                row += 1
                col -= 1
        else:
            if row == 0 and col == len(array[0]) - 1:
                results.append(array[row][col])
                row += 1
                direction = 'down' 
            elif col == len(array[0]) - 1:
                results.append(array[row][col])
                row += 1
                direction = 'down' 
            elif row == 0:
                results.append(array[row][col])
                col += 1
                direction = 'down' 
            else:
                results.append(array[row][col])
                row -= 1
                col += 1
        
    return results

def is_valid_cell(array, row, col):
    return row >= 0 and row <= len(array) - 1 and col >= 0 and col <= len(array[0]) - 1
