class LRUCache:
 
  def __init__(self, capacity: int):
    #define a variable to store max size of the cache      
    self.max_size = capacity
    # intialize a dictionary which would act as a cache
    self.cache = {} 
    # intialize a variable to store the current size of the cache
    self.curr_size = 0
    # initialize a Doubly LinkedList to store the most recently used cache items
    self.items_in_use = DoublyLinkedList()
  
  
  def get(self, key: int) -> int:
    # if key not in cache then return -1
    if key not in self.cache:
      return -1
    else:
      # update the node to be the most recently used in the doubly linked list
      foundNode = self.cache[key]
      self.items_in_use.set_head_to(foundNode)
    # return the value of the Node at the index
    return foundNode.value
  
  def get_most_recent_key(self):
    # return the key of the head of the doubly Linkedlist
    return self.items_in_use.head.key
 
  def put(self, key: int, value: int) -> None:
    node = DoublyLinkedListNode(key, value)
    # check if key is not in cache
    if key not in self.cache:  
      # if the curr size is equal to the max size then evict the least recenet
      if self.max_size == self.curr_size:
        self.evict_least_recent()
      # else increment the current size
      else:
        self.curr_size += 1
      # insert a new Doubly LinkedList Node in the cache in all cases
      self.cache[key] = node
    # else if the key is in cache
    else:
      # replace the key with the new DoublyLinkedList Node's value
      self.cache[key].value = value
    # update the most recent key in all cases. Do this by passing the new Node
    self.update_most_recent(node)
  
  def replace_key(self, key, value):
    # if key is not in cache throw an exception
    if cache[key] is None:
      raise Exception("cannot replace a key which does not exist")
    # else replace the value in the cache with the value of the new doubly linkedlist
    self.cache[key].value = node.value
    
 
  def evict_least_recent(self):
    # get the key of the node to be removed. We can get this from the
    # tail node of the Doubly Linkedlist
    key_to_be_removed = self.items_in_use.tail.key
    value_to_be_removed = self.items_in_use.tail.value
    # remove the tail Node of the DoublyLinkedList
    self.items_in_use.remove_tail()
    # delete the Node from the cache
    del self.cache[key_to_be_removed]
  
  def update_most_recent(self, node):
    # set the node as the head of the doubly linkedlist
    self.items_in_use.set_head_to(node)
    
# define a class for DoublyLinkedList
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
   
  def set_head_to(self, node):
    #if head and the node are the same
    if self.head == node:
      return
    # if head is none
    elif  self.head is None:
      self.head = node
      self.tail = node
    # if the linkedlist has one node
    elif self.head == self.tail:
      self.tail.prev = node
      node.next = self.tail
      node.prev = None
      self.head = node
    # under all other circumstances
    else:
      # if tail is equal to node
      if self.tail == node:
        # remove the tail
        self.remove_tail()
      node.remove_bindings()
      # update pointers as usual
      self.head.prev = node
      node.next = self.head
      self.head = node
    
  def remove_tail(self):
    # if the link list has no nodes
    if self.tail is None:
      raise Exception("Cannot remove tail from an empty linkedlist")
    #if the linked list has one node
    elif self.head == self.tail:
      self.tail = None
      self.head = None
    # if the linkedlist has more than one node
    else:
      new_tail = self.tail.prev
      new_tail.next = None
      self.tail = new_tail
    
 
class DoublyLinkedListNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None
     
  def remove_bindings(self):
    if self.prev is not None:
      self.prev.next = self.next
    if self.next is not None:
      self.next.prev = self.prev
    self.prev = None
    self.next = None
 
 
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
