class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = len(nums1) - len(nums2) - 1
        ptr2 = len(nums2) - 1
        insert_at = len(nums1) - 1
        while ptr1 >= 0 and ptr2 >= 0:
            if nums2[ptr2] >= nums1[ptr1]:
                nums1[insert_at] = nums2[ptr2]
                insert_at -= 1
                ptr2 -= 1
            else:
                nums1[insert_at], nums1[ptr1] = nums1[ptr1], nums1[insert_at]
                insert_at -= 1
                ptr1 -= 1
        while ptr2 >= 0 and insert_at >= 0:
            nums1[insert_at] = nums2[ptr2]
            insert_at -= 1
            ptr2 -= 1
        return nums1
