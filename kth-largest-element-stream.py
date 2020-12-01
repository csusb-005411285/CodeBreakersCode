class KthLargest:

  def __init__(self, k: int, nums: List[int]):
    # init a heap to hold nums
    self.heap = nums
    # init a var to store the kth value
    self.k = k
    # insert values into the heap
    # use the heapq library
    # how do we solve it without heapq library?
    heapq.heapify(self.heap)
    # pop the smallest numbers before k
    while len(self.heap) > k:
      heapq.heappop(self.heap)
    
  def add(self, val: int) -> int:
    # if the size of heap is less than k
    if len(self.heap) < self.k:  
      # insert value into the heap
      heapq.heappush(self.heap, val)
      # return the top value of the heap
      return self.heap[0]
    # else 
    else:
      if val > self.heap[0]:
        # pop the first element
        # insert the new value
        heapq.heapreplace(self.heap, val)
        # return the top of the heap
        return self.heap[0]
      else:
        # return the max. value of the heap
        return self.heap[0]
    
    return -1
  
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

'''
create a bst from the initial array
for each number in the stream, add it to the bst. After adding the number, find the kth largest number.
use the technique to search a number in a bst.
n, n
'''
# Incomplete solution using BST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class KthLargest:

    def __init__(self, k: int, nums: [int]):
        self.k = k
        self.bst = self.create_bst(sorted(nums))

    def create_bst(self, arr):
        if len(arr) == 1:
            return TreeNode(arr[0])
        
        if len(arr) == 0:
            return None
        
        mid = len(arr)//2
        node = TreeNode(arr[mid]) 
        node.left = self.create_bst(arr[:mid])
        node.right = self.create_bst(arr[mid + 1:])

        return node

    def insert(self, val):
        curr_node = self.bst

        while curr_node:
            if val < curr_node.val:
                if not curr_node.left:
                    curr_node.left = TreeNode(val)
                    return
                
                curr_node = curr_node.left
            else:
                if not curr_node.right:
                    curr_node.right = TreeNode(val)
                    return

                curr_node = curr_node.right  
        

    def get_kth_largest(self, node, sorted_arr):
        if not node.left and not node.right:
            sorted_arr.append(node.val)
            return sorted_arr
        
        if node.left:
            self.get_kth_largest(node.left, sorted_arr)
        
        sorted_arr.append(node.val)
        
        if node.right:
            self.get_kth_largest(node.right, sorted_arr)
        
        return sorted_arr

    def add(self, val: int) -> int:
        self.insert(val)
        sorted_arr = []
        self.get_kth_largest(self.bst, sorted_arr)    
        pprint.pprint(sorted_arr)
        return sorted_arr[len(sorted_arr) - self.k]
    
