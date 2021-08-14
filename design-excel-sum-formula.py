class Excel:

    def __init__(self, height: int, width: str):
        self.cells = [{letter: {"value": 0, "sum": None} for letter in string.ascii_uppercase} for h in range(height + 1)]

    def set(self, row: int, column: str, val: int) -> None:
        # populate cell
        self.cells[row][column] = {'value': val, 'sum': None} # 1

    def get(self, row: int, column: str) -> int:
        # get value from the cell
        cell_val = self.cells[row][column]
        # if sum is set
        if cell_val['sum']:
            # process the result
            return self.process_sum_result(cell_val['sum'])
            # return
        return cell_val['value']
        

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        # process the input
        sum_map = self.process_cells(numbers)
        # store it in the cell
        self.cells[row][column]['sum'] = sum_map
        self.cells[row][column]['value'] = 0 # 2
        # return value of the processed input + value at that cell
        return self.process_sum_result(sum_map)

    def process_cells(self, cells) -> dict:
        # init vars
        _map = defaultdict(int)
        # loop input
        for cell in cells:
            # get start and end cell
            start, end = cell, cell
            if ':' in cell:
                start, end = cell.split(':')
            start_row, start_col = int(start[1:]), start[0] # 3
            end_row, end_col = int(end[1:]), end[0] # 3
            # loop rows
            for row in range(start_row, end_row + 1):
                # loop cols
                for col in range(ord(start_col), ord(end_col) + 1):
                    # populate dict
                    _map[(row, chr(col))] += 1
        return _map
    
    def process_sum_result(self, _map):
        res = 0
        # loop dict
        for key, val in _map.items():
            # for key, get value from the cell
            row, col = key
            cell_val = self.get(row, col)
            # mult. the value from cell with value from the dict
            res += cell_val * val
        return res

'''
1. When we set a value, we always set the value to the 'value' property and set 'sum' to None regardless of whether 'sum' is set or not. 
2. When we set the sum, set the 'value' property to 0 regardless of whether the 
'value' was set earlier or not.
3. When we calculate start and end row, always use start[1:] and end[1:] instead of start[1] and end[1] because if start = A12, then using start[1] will give us 1 instead of 12. 
'''
