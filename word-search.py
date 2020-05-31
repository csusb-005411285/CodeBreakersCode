# tc: o(n), sc: o(n)
class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        if len(board) == 0 or len(word) == 0:
            return False
        
        visited = [[False for col in range(len(board[row]))] for row in range(len(board))]
        found_word = False

        for row in range(len(board)):
            for col in range(len(board[row])):
                found_word = self.exist_helper(board, [row, col], visited, word, [board[row][col]])
                if found_word:
                    return True

        return found_word

    def exist_helper(self, board, vertex, visited, word, chars_so_far = []):
        x, y = vertex
        char = ''.join(chars_so_far)
        len_char = len(char)

        if visited[x][y]:
            return False

        if word[:len_char] != char:
            return False

        if len_char == len(word):
            if char == word:
                return True 
            else:
                return False


        visited[x][y] = True 
        neighbors = self.get_neighbors(vertex, board)
        word_found = False 

        for neighbor in neighbors:
            neighbor_x, neighbor_y = neighbor
            word_found = self.exist_helper(board, [neighbor_x, neighbor_y] , visited, word, chars_so_far + [board[neighbor_x][neighbor_y]])
            
            if word_found:
                break

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
