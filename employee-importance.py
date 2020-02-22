"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
  def getImportance(self, employees: List['Employee'], id: int) -> int:
    # the problem is of type, given a graph, find the total distance of all the nodes that can be rached from 
    # the given node. Looks like the solution would be a BFS.
    # init a var which would act as a queue
    empl_queue = []
    # init a var to store the total importance value
    total_imp_value = 0
    # init a dict to store employees as per their id
    empl_dict = collections.defaultdict();
    
    # store the employees in the dict
    for employee in employees:
      empl_dict[employee.id] = employee
    # get the employee object matching the id
    empl_queue.append(id)
    #print(empl_queue.id)
    
    # loop through the list
    while empl_queue: # O(N)
      size = len(empl_queue)
      # while queue is not empty
      for _ in range(size):
        # pop the first element
        employee_id = empl_queue.pop(0)
        print(employee_id)
        # get employee object from employee id
        employee = empl_dict[employee_id]
        # add the importance value of each employee
        total_imp_value += employee.importance
        # add the elemet to the queue
        for subordinate in employee.subordinates:
          empl_queue.append(subordinate)
    
    # return the total importance value
    return total_imp_value
  
  # 2nd attempt
  def getImportance(self, employees: List['Employee'], id: int) -> int:
    # if list of employees is 0
    if len(employees) == 0:
      # then return 0
      return 0
    
    # init a queue
    emp_queue = []
    # init a var to store the total_importance
    total_importance = 0
    visited_emp = 0
    # init a dict to store employee id and the object
    emp_dict = {}
    for employee in employees: # O(n)
      emp_dict[employee.id] = employee
      
    # loop through the list
    for employee in employees: # O(n)
      # find the employee with the id
      # if the employee id matches the given id
      if employee.id == id:
        # store it in a queue
        emp_queue.append(employee) # O(n)
        # perform bfs
        # while queue is not empty
        while emp_queue:
          # pop the left element
          visited_emp = emp_queue.pop(0)
          # add it to the total_importance var
          total_importance += visited_emp.importance
          # loop through all the children
          for subordinate in visited_emp.subordinates: # O(n)
            # add them to the queue
            emp_queue.append(emp_dict[subordinate])
            
    # return total importance
    return total_importance
