class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exclusive_times = [0] * n
        for i, log_item in enumerate(logs):
            id, state, _time = log_item.split(":")
            if state == 'start':
                stack.append([int(id), int(_time)])
            else:
                prev_id, prev_time = stack.pop()
                delta = int(_time) - prev_time + 1
                exclusive_times[prev_id] += int(_time) - prev_time + 1
                if stack:
                    last_id, last_time = stack[-1]
                    exclusive_times[last_id] -= delta 
        return exclusive_times
