# n, n
class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        # build an adjacency list
        adj_list = defaultdict(list) 
        # build an indegree list
        indegree_list = {}
        # init a stack to perform DFS
        stack = deque()
        # init a list to store the courses that can be completed
        courses = []
        
        for i in range(len(prerequisites)):
            indegree_list[prerequisites[i][0]] = 0
            indegree_list[prerequisites[i][1]] = 0

        for i in range(len(prerequisites)): # 0, [[1, 0]]
            adj_list[prerequisites[i][0]].append(prerequisites[i][1])
            indegree_list[prerequisites[i][1]] += 1
        
        for key, value in indegree_list.items():
            if value == 0:
                stack.append(key)

        # loop until the queue is not empty
        while len(stack) > 0:
            # pop element from the queue
            node = stack.pop()
            # store the popped element in a list
            courses.append(node)
            # get the neighbors of the popped element from the adj. list
            for n in adj_list[node]:
                # for each neighbor, reduce their count by 1 in the indegree list
                indegree_list[n] -= 1

                # if a node has a count of 0 in the indegree list
                if indegree_list[n] == 0:
                    # push it to the stack
                    stack.append(n)

            # how do we remove the node from the graph?
        return len(courses) == len(indegree_list.keys()) 
