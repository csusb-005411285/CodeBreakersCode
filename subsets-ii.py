class Solution:
    def __init__(self):
        self.cache = []
        self.prev_len = 0

    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        # sort
        nums.sort()
        # call a helper method
        self.subset_with_dup_helper(nums, len(nums) - 1)
        # return the list
        return self.cache

    def subset_with_dup_helper(self, nums, index): 
        # if index is less than 0
        # base case
        if index < 0:
            return [[]]
        # store the current element at index
        curr_ele = nums[index] 
        # call the recursive function excluding the last element
        res = self.subset_with_dup_helper(nums, index - 1) 
        # store the current length
        curr_len = len(res)
        # since we are going top-down and we are going from the end to the beginning.
        # if the current element equals the previous index
        if curr_ele == nums[index - 1]:
            # get the number of elements added in the previous recursive step.
            diff = curr_len - self.prev_len
            # store the current length, this will be used if the next element is same as this element.
            self.prev_len = len(res)
            # start looping from the element that was added in the last recursive step.
            # we only need to update the elements added in the last step if the current number is
            # same as the previous number.
            for j in range(curr_len - diff, len(res)):
                res.append(res[j] + [curr_ele])
        else:
            self.prev_len = len(res)
            for i in range(len(res) - 1, -1, -1):
                res.append(res[i] + [curr_ele])
        self.cache = res
        return res
