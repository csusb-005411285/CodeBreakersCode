class Solution:
    def __init__(self):
        self.nums = []
        self.counts = []
        
    def countSmaller(self, nums: List[int]) -> List[int]:
        # call the split method
        self.nums = list(enumerate(nums))
        self.counts = [0 for _ in range(len(nums))]
        self.split(0, len(nums) - 1)
        return self.counts
    
    def split(self, start, end):
        # base case. Check if end is before start
        if start >= end:
            return
        # calculate the mid
        mid = start + (end - start)//2
        # split the first half
        self.split(start, mid)
        # split the next half
        self.split(mid + 1, end)
        # call merge
        self.merge(start, end, mid)
        return 
        
    def merge(self, start, end, mid):
        # init vars
        count = 0
        left = start
        right = mid + 1
        res = []
        # perform merge sort
        # while loop
        while left <= mid and right <= end:
            # if left number is smaller than the right
            if self.nums[left][1] <= self.nums[right][1]:
                index = self.nums[left][0]
                # store the count 
                self.counts[index] += count
                # add to result
                res.append(self.nums[left])
                # increment pointer
                left += 1
            # else
            else:
                # increment count
                count += 1
                # add to result
                res.append(self.nums[right])
                # increment pointer
                right += 1
        # parse remaining elements
        # parse left pointer
        while left <= mid:
            index = self.nums[left][0]
            self.counts[index] += count
            res.append(self.nums[left])
            left += 1
        # parse right pointer
        while right <= end:
            res.append(self.nums[right])
            right += 1
        # merge elements
        self.nums[start: end + 1] = res
        return
                
