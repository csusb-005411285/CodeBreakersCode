class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        if len(image) == 0:
            return [[]]
        
        if len(image) == 1 and len(image[0]) == 0:
            return [[]]

        stack = deque()
        stack.append((sr, sc)) 
        og_color = image[sr][sc]

        if og_color == newColor:
            return image

        while stack:
            x, y = stack.popleft() 

            if image[x][y] == og_color: 
                image[x][y] = newColor
            else:
                continue
            
            for i, j in ([x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]):
                if i >= 0 and j >= 0 and i < len(image) and j < len(image[0]):
                    stack.append((i, j)) 

        return image 
