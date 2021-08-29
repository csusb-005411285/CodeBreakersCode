class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = defaultdict(defaultdict)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # add value to snapshot dictionary with current snapshot id as key 
        self.snaps[self.snap_id][index] = val
        
    def snap(self) -> int:
        # increment snapshot id
        self.snap_id += 1
        # return previous snapshot id
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        #  get the value from the snap_id
        curr_snap_id = snap_id
        # if there is no value present in the snap_id, keep checking the previous snap_ids
        # this happens when we call snap back to back
        while curr_snap_id > 0 and index not in self.snaps[curr_snap_id]:
            curr_snap_id -= 1
        # return
        return self.snaps[curr_snap_id][index] if index in self.snaps[curr_snap_id] else 0



# Brute force
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
