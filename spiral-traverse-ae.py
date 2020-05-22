# tc: o(n), sc: o(n)
def spiralTraverse(array):
    '''
    Only work on failing test cases
    '''
    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1
    results = []

    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col, end_col + 1):
            results.append(array[start_row][i])
        start_row += 1

        for j in range(start_row, end_row + 1):
            results.append(array[j][end_col])
        end_col -= 1

        for k in range(end_col, start_col - 1, -1):
            if start_row > end_row:
                break
            results.append(array[end_row][k])
        end_row -= 1

        for l in range(end_row, start_row - 1, -1):
            if start_col > end_col:
                break
            results.append(array[l][start_col])
        start_col += 1

    return result
