class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # init vars
        stack = []
        car_pos = []
        for pos, speed in zip(position, speed):
            car_pos.append((pos, speed))
        car_pos.sort(key = lambda x: x[0])
        # check for invalid inputs
        
        # process
        for i, (pos, speed) in enumerate(car_pos[::-1]):
            time = (target - pos)/speed
            if not stack:
                stack.append(time)
                continue
            if stack and time > stack[-1]:
                stack.append(time)
        # return
        return len(stack)
