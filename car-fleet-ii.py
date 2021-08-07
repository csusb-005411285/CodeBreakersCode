class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        # init vars
        stack = []
        res = []
        # check for invalid inputs
        if len(cars) == 1:
            return [-1.0]
        # process each car
        for car in cars[::-1]:
            pos, speed = car
            # if cars do not collide
            while stack and stack[-1][1] >= speed:
                stack.pop()
            # if cars collide
            # if collision time is greater than the last collision time
            while stack and (stack[-1][0] - pos) / (speed - stack[-1][1]) >= stack[-1][2]:
                    stack.pop()
            # if collision time is less than the last collision time
            if stack:
                collision = (stack[-1][0] - pos) / (speed - stack[-1][1])
                stack.append((pos, speed, collision))
                res.append(collision)    
            # if stack is empty 
            if not stack:
                stack.append((pos, speed, float('inf')))
                res.append(-1)
        # return
        return res[::-1]
