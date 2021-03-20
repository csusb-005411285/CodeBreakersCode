# Iterative
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0
        stack = []
        total = 0
        for i, num in enumerate(nestedList):
            stack.append((num, 1))
        while stack:
            num, depth = stack.pop()
            if num.isInteger():
                total += num.getInteger() * depth
            else:
                for i, val in enumerate(num.getList()):
                    stack.append((val, depth + 1))
        return total
    
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
