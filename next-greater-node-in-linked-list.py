class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        curr = head
        stack = []
        while curr:
            while stack and stack[-1][1] < curr.val:
                index, val = stack.pop()
                res[index] = curr.val
            stack.append((len(res), curr.val))
            res.append(0)
            curr = curr.next
        return res
