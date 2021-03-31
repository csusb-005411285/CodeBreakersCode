class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        return self._clean_room(robot, 0, 0, 0, 1, visited)
    
    def _clean_room(self, robot, x, y, next_x, next_y, visited):
        if (x, y) in visited:
            return
        robot.clean()
        visited.add((x, y))
        for _ in range(4):
            neigh_x = x + next_x
            neigh_y = y + next_y
            if (neigh_x, neigh_y) not in visited and robot.move():
                self._clean_room(robot, neigh_x, neigh_y, next_x, next_y, visited)
                self.go_back(robot)
            robot.turnLeft()
            next_x, next_y = -next_y, next_x
        return
    
    def go_back(self, robot):
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()
