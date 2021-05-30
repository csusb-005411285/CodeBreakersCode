class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        is_not_present = True 
        if val in self.list:
            is_not_present = False
        self.list.append(val)
        self.map[val].add(len(self.list) - 1)
        return is_not_present

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.list:
            return False
        # get index of last element
        last_index = len(self.list) - 1
        # discard index last of last element
        last_element = self.list[last_index]
        # get index of element to be deleted
        delete_index = self.map[val].pop()
        self.map[val].discard(delete_index)
        # swap values
        self.list[last_index], self.list[delete_index] = self.list[delete_index], self.list[last_index]
        # pop the last element
        self.list.pop()
        # discard index of element to be deleted
        # add the index of the element to be deleted to the value pointed last element in the hash map
        self.map[last_element].add(delete_index)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.list)
