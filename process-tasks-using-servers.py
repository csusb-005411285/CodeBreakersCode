# A correct solution that TLEs.
# This solution is easier to understand, but does not pass all test case; it is correct but TLEs at larger edge cases.
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free_heap = []
        busy_heap = []
        ans = []
        timer = 0
        curr_index = 0
        queue = deque()
        for idx, weight in enumerate(servers):
            heappush(free_heap, (weight, idx))
        while len(ans) != len(tasks):
            while curr_index <= timer and curr_index < len(tasks):
                queue.append((curr_index, tasks[curr_index]))
                curr_index += 1
            while busy_heap and busy_heap[0][0] <= timer:
                _, server_weight, server_id = heappop(busy_heap)
                heappush(free_heap, (server_weight, server_id))
            while not queue and busy_heap:
                timer = busy_heap[0][0]
                continue
            while queue and free_heap:
                server_weight, server_id = heappop(free_heap)
                task_id, task_time = queue.popleft()
                heappush(busy_heap, (timer + task_time, server_weight, server_id))
                ans.append(server_id)
            timer += 1
        return ans

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # a heap to hold the servers 
        server_heap = []
        # a heap to hold the busy servers
        busy_heap = []
        # a queue to hold the tasks
        tasks_deque = deque()
        # a list to store the results
        ans = []
        # a variable to hold the time
        time = 0
        # to keep track of tasks
        offset = 0
        # add the servers to the heap
        # use a tuple of server weight, server id
        for _id, weight in enumerate(servers):
            heappush(server_heap, (weight, _id))
        tasks = deque(tasks)
        # loop until we have processed all the tasks
        while len(ans) < len(tasks):
            # bring all tasks that are ready to run to the task queue
            # if the index of the task list is smaller than the time so far, add it to the task queue
            offset = len(ans) + len(tasks_deque) # 1.
            for i in range(offset, len(tasks)):
                if i <= time:
                    tasks_deque.append(tasks[i])
                else:
                    break
                    
            # add busy servers that are now free to the servers list
            # check the server at the top of the heap to find out its time.
            # if the time is smaller than the current time
            # add it to the free servers heap
            while busy_heap and busy_heap[0][0] <= time:
                _, weight, _id = heappop(busy_heap)
                heappush(server_heap, (weight, _id))
                
            # if no servers are free
            # set the time to  the time at the top of the busy servers heap
            # continue
            # This step is to prevent TLE.
            if not server_heap:
                time = busy_heap[0][0]
                continue
            
            # as long as there are tasks in the task queue and servers in the servers heap
            # get task from task queue
            # get server from top of heap
            # add server index to result set
            # add server to busy heap. add a tuple containing (current time + time to complete the task, server weight, server index)
            while tasks_deque and server_heap:
                task_time = tasks_deque.popleft()
                weight, _id = heappop(server_heap)
                ans.append(_id)
                heappush(busy_heap, (time + task_time, weight, _id))
            time += 1
        # return ans
        return ans    
    
'''
1. We use this len(ans) + len(tasks_deque) because each task will either be already processed or will be ready for processing. However, we need the tasks that are not yet processed. 
'''
