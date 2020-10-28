class Solution:
    def __init__(self):
        self.subset = []

    def subsets(self, nums: [int]) -> [[int]]:
        # use a var to store the subsets
        # use a helper method to compute
        self.subsets_helper(nums, len(nums) - 1)
        # return the subsets
        pprint.pprint(self.subset)
        return self.subsets
 
    def subsets_helper(self, nums, index):
        # if index is less than 0
        if index < 0:
            # return empyt set
            return [[]]
        # reduce the input by 1, starting from the end
        # store the element at the index
        ele = nums[index] 
        # call the recursive method
        # store the result of the recursive method
        result = self.subsets_helper(nums, index - 1)
        # append the current element to each element of the result
        for i in range(len(result)): 
            res = result[i] 
            result.append(result[i] + [ele]) 
        self.subset = result
        # return the result
        return self.subset 
