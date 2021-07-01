class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        # loop
        for i, num in enumerate(temperatures):
            # If the current value is greater than the value at the top of the stack
            while stack and num > stack[-1][1]:
                # pop the element
                index, temperature = stack.pop()
                # caclulate the diff in indices
                res[index] = i - index
            # add to stack
            stack.append((i, num))
        return res
