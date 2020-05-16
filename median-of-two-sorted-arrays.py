class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        l1 = len(nums1)
        l2 = len(nums2)

        left = 0
        right = len(nums1)
        
        while left <= right:
            m1 = left + ((right - left) // 2)
            m2 = ((l1 + l2 + 1)// 2) - m1

            val_m1 = float('inf') if m1 == l1 else nums1[m1]
            val_m2 = float('inf') if m2 == l2 else nums2[m2]

            left_val_m1 = float('-inf') if m1 == 0 else nums1[m1 - 1]
            left_val_m2 = float('-inf') if m2 == 0 else nums2[m2 - 1]

            if left_val_m1 <= val_m2 and left_val_m2 <= val_m1:
                if (l1 + l2) % 2 == 0:
                    return (max(left_val_m1, left_val_m2) + min(val_m1, val_m2)) / 2
                else:
                    '''
                    made a mistake here
                    '''
                    return max(left_val_m1, left_val_m2) 

            elif left_val_m1 > val_m2:
                right = m1 - 1
            elif left_val_m2 > val_m1:
                left = m1 + 1
            else:
                continue
        
        raise Exception('Arrays not sorted'
