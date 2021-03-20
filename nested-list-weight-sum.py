class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0
        return self._depth_sum(nestedList, 1)
    
    def _depth_sum(self, lst, depth):
        total = 0
        for i, num in enumerate(lst):
            if num.isInteger():
                total += num.getInteger() * depth
            else:
                total += self._depth_sum(num.getList(), depth + 1)
        return total
