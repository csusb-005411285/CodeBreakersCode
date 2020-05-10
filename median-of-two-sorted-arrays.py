class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        len_num1 = len(nums1)
        len_num2 = len(nums2)

        left = 0
        right = len_num1 
        while left <= right:
            partition_x = left + (right - left) // 2
            # + 1 is to handle the even odd cases correctly
            partition_y = ((len_num1 + len_num2 + 1) // 2) - partition_x
        
            x = float('inf') if partition_x == len_num1 else nums1[partition_x]
            left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]

            y = float('inf') if partition_y == len_num2 else nums2[partition_y]
            left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]

            if left_x <= y and left_y <= x:
                if (len_num1 + len_num2)%2 == 0:
                    return (max(left_x, left_y) + min(x, y))/2 
                else:
                    return max(left_x, left_y)
            elif left_x > y:
                right = partition_x - 1
            else:
                left = partition_x + 1

        raise Exception('Arrays not sorted')
