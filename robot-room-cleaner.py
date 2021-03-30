class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        return self._clean_room(robot, (0, 0), 0, 1, visited)
        
    def _clean_room(self, robot, vert, x, y, visited):
        row, col = vert
        if vert in visited:
            return None
        visited.add(vert)
        robot.clean()
        for i in range(4):
            if (row + x, col + y) not in visited and robot.move():
                self._clean_room(robot, (row + x, col + y), x, y, visited)
                self.go_back(robot)
            robot.turnRight()
            x, y = -y, x
        return None
    
    def go_back(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
        
        
        
