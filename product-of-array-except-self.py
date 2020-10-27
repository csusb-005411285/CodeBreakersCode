class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 1
        if len(nums) == 1:
            return nums[0]
        # use a list to store the results
        prod = [1 for _ in range(len(nums))]
        # use two vars to store the rolling prods
        fp = nums[0]
        bp = nums[-1] 
        # loop through the list, start from 1
        for i in range(1, len(nums)):
            # the value at each index is the rolling prod so far
            prod[i] = fp
            # calculate the rolling sum upto current the current index
            fp *= nums[i]
        # loop backwards
        for j in range(len(nums) - 2, -1, -1):
            # the value at each index is the rolling prod upto the prev index
            # prod the rolling sum to the existing value in the results
            prod[j] = prod[j] * bp
            # calculate the rolling prod at the curr index
            bp = bp * nums[j]
        # return results list
        return prod 
