class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        pairs = []
        arr.sort()
        min_diff = sys.maxsize
        for i, num in enumerate(arr[1:], start=1):
            if num - arr[i - 1] < min_diff:
                min_diff = num - arr[i - 1]
        for i, num in enumerate(arr[1:], start=1):
            if num - arr[i - 1] == min_diff:
                pairs.append([arr[i - 1], num])
        return pairs
    
