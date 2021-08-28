class SnapshotArray:

    def __init__(self, length: int):
        # init a hash map instead of list
        self.map = defaultdict(int)
        for i in range(length):
            self.map[i] = 0
        # a hashmap to store the snapshots
        self.snapshots = defaultdict()
        # var to store the snap id
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        # set the value at index
        self.map[index] = val
        
    def snap(self) -> int:
        # add the inital hashmap to the snapshot hashmap
        self.snapshots[self.snap_id] = list(self.map.values())
        # increment snap id
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        #pp(self.snapshots)
        # get the value from snapshot hashmap
        snapshot = self.snapshots[snap_id]
        # get the value at the index from the value we got from above
        return snapshot[index]
