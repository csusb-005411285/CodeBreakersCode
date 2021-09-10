class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # init vars
        answers = []
        # initial checks
        
        # process
        # loop through number of cols
        for i in range(len(grid[0])):    
            # track row and col
            row = 0
            col = i
            # while row and col are within bounds
            while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                # if the cell has 1 and the right cell has 1
                if grid[row][col] == 1 and col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                    # move to the bottom right
                    row += 1
                    col += 1
                # if the cell has -1 and the left cell has -1
                elif grid[row][col] == -1 and col - 1 >= 0 and grid[row][col - 1] == -1:
                    # move to bottom left
                    row += 1
                    col -= 1
                # if the two conditions do not satisfy
                else:
                    # break
                    break
            # if row is the last one, add col to answers
            # if not add -1
            column = col if row == len(grid) else -1
            answers.append(column)
        # return
        return answers
