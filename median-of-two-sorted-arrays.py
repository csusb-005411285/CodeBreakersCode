class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        left = 0
        right = len(nums1)
        # why do we need the combined len?
        combined_len = len(nums1) + len(nums2)
        # why do we run bs on first array?
        while left <= right:
            mid1 = left + (right - left)//2
            # why do we subtract?
            mid2 = ((combined_len + 1)//2) - mid1
            
            # why do we need this step?
            # As the right pointer starts at the last index + 1
            val1 = nums1[mid1] if mid1 < len(nums1) else float('inf')
            val2 = nums2[mid2] if mid2 < len(nums2) else float('inf')
            
            left_val1 = float('-inf') if mid1 - 1 < 0 else nums1[mid1 - 1]
            left_val2 = float('-inf') if mid2 - 1 < 0 else nums2[mid2 - 1]
            
            if left_val1 <= val2 and left_val2 <= val1:
                if combined_len%2 == 0:
                    return (max(left_val1, left_val2) + min(val1, val2))/2
                else:
                    # why max and not min?
                    return max(left_val1, left_val2)
            
            if left_val1 > val2:
                right = mid1 - 1
            else:
                left = mid1 + 1
        return -1

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
                    return max(left_val_m1, left_val_m2) 

            elif left_val_m1 > val_m2:
                right = m1 - 1
            elif left_val_m2 > val_m1:
                left = m1 + 1
            else:
                continue
        
        raise Exception('Arrays not sorted'
