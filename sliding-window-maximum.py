class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        for i, num in enumerate(nums):
            while queue and i - queue[0] >= k:
                queue.popleft()
            while queue and num > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            ans.append(nums[queue[0]])
        return ans[k - 1:]
