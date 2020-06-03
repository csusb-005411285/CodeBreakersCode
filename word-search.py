# tc: o(n), sc: o(n)
class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        visited = [[False for col in range(len(board[row]))] for row in range(len(board))]
        word_exists = False

        for row in range(len(board)):
            for col in range(len(board[row])):
                word_exists = self.exist_helper(board, [row, col], visited, word, board[row][col])

                if word_exists:
                    return True

        return word_exists

    def exist_helper(self, board, vertex, visited, word, chars_so_far):
        x, y = vertex
        
        if visited[x][y]:
            return False

        if not word.startswith(chars_so_far):
            return False
        
        if chars_so_far == word:
            return True

        visited[x][y] = True
        neighbors = self.get_neighbors(vertex, board)
        word_found = False

        for neighbor in neighbors:
            neigh_x, neigh_y = neighbor
            word_found = self.exist_helper(board, [neigh_x, neigh_y], visited, word, chars_so_far + board[neigh_x][neigh_y])

            if word_found:
                return True
        
        visited[x][y] = False
        return word_found
   
    def get_neighbors(self, vertex, board):
        neighbors = []
        x, y = vertex

        if x > 0:
            neighbors.append([x - 1, y])

        if y > 0:
            neighbors.append([x, y - 1])

        if x < len(board) - 1:
            neighbors.append([x + 1, y])

        if y < len(board[x]) - 1:
            neighbors.append([x, y + 1])

        return neighbors 

