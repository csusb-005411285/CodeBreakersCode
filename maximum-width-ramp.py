class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        a = A
        index_list = []
        value_map = defaultdict(int)
        min_index = float('inf')
        max_width = 0
        for i, val in enumerate(a):
            value_map[i] = val
        sorted_values = dict(sorted(value_map.items(), key=lambda item: item[1]))
        min_index = float('inf')
        for index, value in sorted_values.items():
            max_width = max(max_width, index - min_index)
            if index < min_index:
                min_index = index
        return max_width
    
class Solution:
    def maxWidthRamp(self, A: [int]) -> int:
        a = A
        max_ramp = 0 
        stack = deque()

        for i in range(len(a)):
            if not stack or a[stack[-1]] > a[i]:
                stack.append(i)
        
        for j in range(len(a) - 1, -1, -1):
            while stack and a[j] >= a[stack[-1]]:
                max_ramp = max(max_ramp, j - stack[-1])
                stack.pop()

        return max_ramp
