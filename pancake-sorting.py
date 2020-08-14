class Solution:
    def pancakeSort(self, a: [int]) -> [int]:
        res = []
        for i in range(len(a) - 1, -1, -1): # 3
            max_ele = max(a[:i + 1]) # 4
            max_ele_index = a.index(max_ele) # 2 
            self.flip(a, max_ele_index + 1) # [3, 2, 4], 3
            res.append(max_ele_index + 1) # 3 
            self.flip(a, i + 1) # [3, 2, 4], 
            res.append(i + 1) # 

        pprint.pprint(a)
        return res        

    def flip(self, a, k):
        left = 0
        right = k - 1
        while left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1

        return a
