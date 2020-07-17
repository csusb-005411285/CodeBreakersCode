class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        cur = self
        out = ""
        while(cur):
            out += str(cur.val)
            cur = cur.next
        return out

#1 -> 2 -> 3
#3 -> 2 -> 1 -> None

# None

# 1 ->


# cur - None     <- 1  <- 2  <- 3
# prev - 3
# next = None


# cur - None
# prev - 1
# next - None
def reverseLinkedList(head):
    cur = head
    prev = None
    while cur:
		Next = cur.next
		cur.next = prev
		prev = cur
		cur = Next

    return prev

#make List of 10 Node objects
head = Node("head")
cur = head
for i in range(10):
    cur.next = Node(i)
    cur = cur.next
print(head.next)
head.next = reverseLinkedList(head.next)
print(head.next)
