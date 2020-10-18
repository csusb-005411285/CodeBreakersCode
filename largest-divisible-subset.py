class Solution:
    def largestDivisibleSubset(self, nums: [int]) -> [int]:
        if len(nums) <= 1:
            return nums
        # sort the array
        nums.sort()
        # init a cache
        # the key of the cache would be the nums and the value would be a tuple consisting of
        # the lenght of largest divisible subset and the subset
        cache = {}
        for i in nums:
            cache[i] = (1, [i])
        # init a var to store the max length
        max_subset_len = float('-inf')
        # init a var to store the subset
        subset = []
        # loop through the list
        for i in range(1, len(nums)):
            # loop until the current element
            for j in range(0, i):
                # for each element, calculate the largest divisible subset
                # the first value of the tuple would be the number of divisible subsets of the 
                # prev element + 1
                # the second value of the tuple would be the subsets which are formed by the previous
                # element and the current element added to it
                # only update the cache if the number of divisible subsets of the previous element + 1
                # is greater than the current value in the cache for the current element.
                if nums[i] % nums[j] == 0:
                    if cache[nums[j]][0] + 1 >= cache[nums[i]][0]:
                        cache[nums[i]] = (cache[nums[j]][0] + 1, cache[nums[j]][1] + [nums[i]])

        # loop through the cache
        for key, value in cache.items():
            # find the tuple whose first element has the largest value
            if value[0] >= max_subset_len:
                max_subset_len = value[0] 
                # store the second value of that tuple   
                subset = value[1] 
        
        # return the second value of the tuple
        return subset
