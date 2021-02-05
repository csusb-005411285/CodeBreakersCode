class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.num_map = defaultdict(int)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.num_map:
            return False
        self.nums.append(val)
        index = len(self.nums) - 1
        self.num_map[val] = index
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.num_map:
            return False
        index_to_remove = self.num_map[val]
        last_index = len(self.nums) - 1
        value_at_last_index = self.nums[-1]
        self.nums[index_to_remove], self.nums[last_index] = self.nums[last_index], self.nums[index_to_remove]
        self.num_map[value_at_last_index] = index_to_remove
        self.nums.pop()
        del self.num_map[val]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choices(self.nums)[0]
