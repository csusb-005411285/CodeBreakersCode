class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:   
        task_map = Counter(tasks)
        sorted_task_map = dict(sorted(task_map.items(), key = lambda x : x[1]))
        task_values = list(sorted_task_map.values())
        max_freq = task_values.pop() - 1
        idle_slots = max_freq * n
        while task_values:
            idle_slots -= min(max_freq, task_values.pop())
        idle_slots = max(0, idle_slots)
        return len(tasks) + idle_slots
        
