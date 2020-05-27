# tc: o(n), sc: o(1)
def shiftLinkedList(head, k):
    if k == 0:
        return head

    start = head
    end, length = get_last_node_linked_list(head)

    if k == length:
        return head

    kth_node = get_kth_node_linked_list(head, k, length)
    head = rotate(start, end, kth_node) 
    return head 

def rotate(start, end, kth_node):
    end.next = start

    if kth_node:
        start = kth_node.next
        kth_node.next = None
        
    return start

def get_kth_node_linked_list(head, k, length):
    if k < 0:
        remainder = abs(k) % length

        if remainder == 0:
            remainder = length
            
        k_from_end = remainder
    else:
        remainder = k % length
        k_from_end = length - remainder

    i = 0
    curr_node = head

    while i < k_from_end - 1 and curr_node:
        curr_node = curr_node.next
        i += 1

    return curr_node

def get_last_node_linked_list(head):
    curr_node = head
    length = 1
    
    while curr_node.next:
        curr_node = curr_node.next
        length += 1
    
    return [curr_node, length]
