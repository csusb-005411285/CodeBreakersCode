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
    # init a var to store the importance
    
    # init a queue, store the first employee object
    
    # init a var to store the visited employees
    
    # loop throught the employees queue
      
      # pop the first element
      
      # check if the element is not visited
      
        # then insert it in the visited array
        
      # calcualate the importance
      
      # loop through the subordinate
      
        # add them to the queue
      
