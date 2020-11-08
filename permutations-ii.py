class Solution:
    def __init__(self):
        self.permutation = []

    def permuteUnique(self, nums: [int]) -> [[int]]:
        # call helper
        nums.sort()
        self.permute_unique_helper(nums, [], len(nums))
        # return list
        return self.permutation

    def permute_unique_helper(self, nums, curr_perm, target):
        # if current permutations length is equal to target 
        # base case
        if len(curr_perm) == target: 
            self.permutation.append(curr_perm) 
            return

        # loop
        for i in range(len(nums)): 
            # check if current number is not equal to the next number
            if (i + 1 < len(nums) and nums[i] != nums[i + 1]) or i == len(nums) - 1: 
                # call recursive function
                self.permute_unique_helper(nums[:i] + nums[i + 1:], curr_perm + [nums[i]], target) 
        return

    # check the previous number for duplicates
    def permute_unique_helper(self, nums, curr_comb):
        if len(nums) == 0:
            self.permutations.append(curr_comb)
            return
        for i in range(len(nums)):
            if (i - 1 >= 0 and nums[i - 1] == nums[i]):
                continue
            self.permute_unique_helper(nums[:i] + nums[i + 1:], curr_comb + [nums[i]])
        return
