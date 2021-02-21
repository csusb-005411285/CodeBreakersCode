class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        if head.next is head:
            new_node = Node(insertVal)
            new_node.next = head
            head.next = new_node
            return head
        prev = head
        curr = head.next
        found = False
        while True:
            if prev.val <= insertVal <= curr.val:
                found = True
                break
            if prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    found = True
                    break
            prev = prev.next
            curr = curr.next
            if prev is head:
                break
        prev.next = Node(insertVal, curr)
        return head
