n1 = m - 1
        n2 = n - 1
        right = len(nums1) - 1
        while n1 >= 0 and n2 >= 0:
            v1 = nums1[n1]
            v2 = nums2[n2]
            if v2 > v1:
                nums1[right] = v2
                right -= 1
                n2 -= 1
            else:
                nums1[right] = v1
                right -= 1
                n1 -= 1
        if n1 < 0 and n2 >= 0:
            while right >= 0 and n2 >= 0:
                nums1[right] = nums2[n2]
                n2 -= 1
                right -= 1
        return nums1
