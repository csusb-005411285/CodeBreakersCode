class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        curr = head # -1

        # loop until the end of the list
        while curr and curr.next: # 5, 0
            # if the curr node is greater than the next node: # 1 -> 3
            # we consider the next node to be out of order, and we would try to place it
            # in the correct location
            if curr.val > curr.next.val: # 5 > 0
                # store the next node in a var, the next node would be the target node # 2
                target = curr.next # 0
                # initialize a variable that would act as a temp curr node, set it to head # 4
                runner = head # -1
                # loop from the start with the intention of placing the target node
                # use a prev variable to store the node before the curr node
                # loop until the curr node is less than target: # 
                prev = None
                while runner.val < target.val: # 3 < 0
                    prev = runner # -1
                    runner = runner.next # 3

                # if we are here that means, the target should be placed before the curr node
                # 4 -> 2
                # $    t
                next_target = target.next # n
                # set the curr node to the next node of target node - curr -> 1
                if target:
                    target.next = runner # 0 -> 3
                    
                if runner is head:
                    head = target
                    
                # set the next node pf prev to point to target
                if prev:
                    prev.next = target # -1 -> 0
                # set the next node of temp curr node to point to next node of target node - 4 -> 1
                if curr:
                    curr.next = next_target
            else:
                curr = curr.next # 5
        
        return head
