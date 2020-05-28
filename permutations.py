class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        permutations = []
        self.permutations_helper(nums, [], permutations)
        return permutations

    
    def permutations_helper(self, nums, permutation, permutations):
        if not nums:
            permutations.append(permutation)
            return

        for i in range(len(nums)):
            self.permutations_helper(nums[:i] + nums[i + 1:], permutation + [nums[i]], permutations)
        return

# tc: o(n!), sc: o(n)
class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        permutations = []
        self.permute_helper(len(nums), [], nums, permutations)
        return permutations

    def permute_helper(self, target_len, curr_selection = [], choices = [], permutations = []):
        if len(curr_selection) == target_len:
            permutations.append(curr_selection)
            return

        for i in range(len(choices)):
            self.permute_helper(target_len, curr_selection + [choices[i]], [] + choices[:i] + choices[i + 1:], permutations)

        return
