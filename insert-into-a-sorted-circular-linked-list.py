class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        if head.next is head:
            new_node = Node(insertVal)
            if insertVal < head.val:
                new_node.next = head
                head.next = new_node
            else:
                head.next = new_node
                new_node.next = head
            return head
        curr = head.next
        prev = head
        found = False
        while True:
            if prev.val <= insertVal <= curr.val:
                found = True
            elif prev.val > curr.val:
                if insertVal <= curr.val:
                    found = True
                elif insertVal >= prev.val:
                    found = True
            if found:
                new_node = Node(insertVal)
                prev.next = new_node
                new_node.next = curr
                return head
            prev, curr = curr, curr.next
            if prev == head:
                break
        # for cases like [3, 3, 3, 3] 0
        prev.next = Node(insertVal, curr)
        return head
