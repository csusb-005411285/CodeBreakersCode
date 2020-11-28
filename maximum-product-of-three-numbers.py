class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max_digit = max(nums[0], nums[1])
        min_digit = min(nums[0], nums[1])
        max_prod_two = nums[0] * nums[1]
        min_prod_two = nums[0] * nums[1]
        max_prod_three = nums[2] * nums[1] * nums[0]
        for i, v in enumerate(nums[2:], start=2):
            max_prod_three = max(max_prod_three, max(max_prod_two * v, min_prod_two * v))
            max_prod_two = max(max_prod_two, v * max_digit, v * min_digit)
            min_prod_two = min(min_prod_two, v * min_digit, v * max_digit)
            max_digit = max(max_digit, v)
            min_digit = min(min_digit, v)
        return max_prod_three 
