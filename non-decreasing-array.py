class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        arr = nums
        for i in range(len(arr) - 1):
            num = arr[i]
            if arr[i] > arr[i + 1]:
                count += 1
                if i - 1 >= 0 and i + 2 < len(arr) and arr[i - 1] > arr[i + 1] and arr[i] > arr[i + 2]:
                    return False
            if count > 1:
                return False
        return True
