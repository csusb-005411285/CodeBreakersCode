class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # init vars
        heap = []
        order = []
        timer = 1
        tasks_with_id = defaultdict(list)
        j = 0
        # perform initial checks
        if len(tasks) == 1:
            return [0]
        # process
        for i, (start_time, execution_time) in enumerate(tasks):
            tasks_with_id[start_time].append((i, start_time, execution_time))  
        sorted_tasks = dict(sorted(tasks_with_id.items(), key = lambda x: x[0])) # 1.
        for start_time, items in sorted_tasks.items():
            while heap and start_time > timer: # 3.
                execution, index, start = heappop(heap)
                order.append(index)
                timer = max(timer, start) + execution # 4.
            for (i, start, execution) in sorted_tasks[start_time]:
                heappush(heap, (execution, i, start)) # 2.
        while heap:
            execution, index, start = heappop(heap)
            order.append(index)
        # return order
        return order
