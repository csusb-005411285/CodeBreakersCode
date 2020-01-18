class Node:
  def __init__(self, key, value, nxt = None):
    self.key = key
    self.value = value
    self.nxt = nxt

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # initlaize a map
        self.map = [Node("dummy", "dummy")]
     
    def hashed_index(self, key):
      # mod key with the length of the map
      return key % len(self.map)
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # get a hash of the index
        index = self.hashed_index(key)
        if self.map[index] is None:
          self.map[index] = Node("dummy", "dummy")
        # check if an element exists in that index
        element = self.map[index]
        # loop until the next Node is null
        while element.nxt:  
          # insert the key and value to the next Node
          if element.nxt.key == key:
            element.nxt.value = value
            return
          element = element.nxt
        # insert a Node as a next element to the Linkedlist
        element.nxt = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        # get the hashed index
        index = self.hashed_index(key)
        # get the first Node from that index which should be the "dummy" Node
        curr = self.map[index]
        # loop through the linkedlist
        while curr.nxt:  
          # as you loop through the Linkedlist check if the value is present
          if curr.nxt.key == key:
            return curr.nxt.value
          curr = curr.nxt
        # return the value or None
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # get the hashed index
        index = self.hashed_index(key)
        # get the value from the index
        value = self.map[index]
        # store this value in the prev variable. This is the dummy Node hence the prev var
        prev_node = value
        # store the next value in the curr variable
        curr = prev_node.nxt
        # loop until the current Node is None
        while curr is not None:  
          # if we find the key set the prev nodes pointer to the next of
          if curr.key == key:
            # the current nodes pointer
            prev_node.nxt = curr.nxt
          # if we do not find a value then keep looping
          prev = curr
          curr = curr.nxt
          
    # def __str__(self):
        # initalize a variable to store the output
        # loop from 0 to the end of the map
        # loop through the linked list in each index
        # append the values
        # return the variable


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
