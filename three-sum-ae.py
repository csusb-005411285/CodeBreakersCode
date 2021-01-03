# Leetcode
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i, num in enumerate(nums):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + num + nums[right] > 0:
                    right -= 1
                elif nums[left] + num + nums[right] < 0:
                    left += 1
                else:
                    triplets.append([nums[left], num, nums[right]])
                    left += 1
                    right -= 1
                    while left < len(nums) and left - 1 >= 0 and nums[left] == nums[left - 1]:
                        left += 1
        return triplets

def threeNumberSum(array, targetSum):
    triplets = [] #n
    array.sort() # nlogn
    for i in range(len(array) - 2): #n
        result = three_number_sum_helper(array, targetSum, i)
        if result:
            triplets.extend(result)
    
    if len(triplets) == 0:
        return []

    return triplets

def three_number_sum_helper(array, target, curr):
    start = curr + 1
    end = len(array) - 1
    result = []
    while start < end: #n
        if array[curr] + array[start] + array[end] == target:
            result.append([array[curr], array[start], array[end]])
            start += 1
            end -= 1
        elif array[curr] + array[start] + array[end] > target:
            end -= 1
        else:
            start += 1
    return result 
