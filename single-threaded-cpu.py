# Tuple based solution
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_map = defaultdict(list)
        order = []
        timer = 0
        heap = []
        tasks_tuple = []
        for i, task in enumerate(tasks):
            start_task_at, processing_time = task
            tasks_tuple.append((start_task_at, processing_time, i))
        tasks_tuple_sorted = sorted(tasks_tuple, key = lambda x: x[0])
        tasks_deque = deque(tasks_tuple_sorted)
        while len(order) != len(tasks):
            while tasks_deque and timer >= tasks_deque[0][0]:
                tasks_starting_at_time, processing_time, task_id = tasks_deque.popleft()
                heappush(heap, (processing_time, task_id))
            if heap:
                processing_time, task_id = heappop(heap)
                order.append(task_id)
                timer += processing_time
            else:
                timer = tasks_deque[0][0]
        return order

# Alternate solution
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # init vars
        # heap
        heap = []
        # timer
        timer = 0
        # order of tasks
        order = []
        i = 0
        # initial checks
        
        # process
        # sort tasks by enque time
        for j, task in enumerate(tasks):
            task.append(j)
        sorted_tasks = sorted(tasks, key = lambda x: x[0])
        # set timer to first task
        timer = sorted_tasks[0][0] 
        # loop through sorted tasks
        while i < len(sorted_tasks): 
            # while timer equals the enque time
            while i < len(sorted_tasks) and timer >= sorted_tasks[i][0]: 
                # add to heap
                # add a tuple of processing time and index
                heappush(heap, (sorted_tasks[i][1], sorted_tasks[i][2])) 
                i += 1
            # while heap has elements
            if heap: 
                # remove
                time, index = heappop(heap) 
                # add to final result, add index
                order.append(index) 
                # increment timer
                timer += time 
            else:
                timer = sorted_tasks[i][0]
        while heap:
            time, index = heappop(heap) 
            # add to final result, add index
            order.append(index) 
        # return order
        return order

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
