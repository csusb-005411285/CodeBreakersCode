class Solution:
    def checkIfExist(self, arr: [int]) -> bool:
        hash_map = {}
        hash_map = Counter(arr)

        for i in range(len(arr)):
            m = arr[i]
            n = 2 * m

            if m == 0:
                if hash_map[m] == 2:
                    return True
                else:
                    continue

            if n in hash_map:
                return True 

        return False
