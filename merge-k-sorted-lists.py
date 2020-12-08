class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        heap = []
        dummy_head = ListNode('inf')
        curr = dummy_head
        for i, lst in enumerate(lists):
            if lst is not None:
                heappush(heap, (lst.val, i, lst))
        while heap:
            val, index, lst = heappop(heap)
            curr.next = lst
            curr = curr.next
            if lst.next is not None:
                heappush(heap, (lst.next.val, index, lst.next))
        return dummy_head.next
