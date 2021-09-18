class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        arr_map = defaultdict(int)
        count = 0
        for i, num in enumerate(arr):
            if num <= 0 and num * 2 in arr_map:
                arr_map[num * 2] -= 1
                if arr_map[num * 2] == 0:
                    del arr_map[num * 2]
                count += 1
            elif num > 0 and num/2 in arr_map:
                arr_map[num / 2] -= 1
                if arr_map[num / 2] == 0:
                    del arr_map[num / 2]
                count += 1
            else:
                arr_map[num] += 1
        return True if count == len(arr)//2 else False
