class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # init vars
        heap = []
        min_range_val = sys.maxsize
        max_range_val = float('-inf')
        _max = float('-inf')
        min_diff = sys.maxsize
        # inital checks
        # if nums has one element
        # calculate the mid
        # compare the mid with the prev. and next number
        # return the range that has the smaller diff
        
        # process
        # add values from the first index to the heap
        # heap will contain a tuple of index of row, index of col, and value
        for i, num in enumerate(nums):
            heappush(heap, (num[0], i, 0))
            _max = max(_max, num[0]) # 2.
        # loop while heap has elements
        while heap and len(heap) == len(nums): # 1.
            # pop from heap
            val, row_idx, col_idx = heappop(heap)
            # calculate the min diff
            if _max - val < min_diff:
                # if diff is smaller, store the values
                min_range_val = val
                max_range_val = _max
                min_diff = max_range_val - min_range_val
            # check if next element exists
            # if index + 1 < len of col
            if col_idx + 1 < len(nums[row_idx]):
                val = nums[row_idx][col_idx + 1]
                # calculate the max value
                _max = max(_max, val)
                # add the next element to heap
                heappush(heap, (val, row_idx, col_idx + 1))
        # return
        return [min_range_val, max_range_val]
    
'''
1. The number of elements in the heap should be equal to the numbers of rows of the input.
2. Do not forget to calculate the max. value as you enter elements to the heap. 
'''
