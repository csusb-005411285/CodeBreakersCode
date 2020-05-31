# tc: o(n), sc: o(1)
def shiftLinkedList(head, k):
    len_linked_list = get_length_linked_list(head)
    location_linked_list =  get_linked_list_position(len_linked_list, k)
    tail, new_head = get_new_head_tail(head, location_linked_list, len_linked_list)
    last_node = get_length_linked_last_node(head, len_linked_list)

    last_node.next = head
    tail.next = None
    head = new_head 

    return head

def get_length_linked_last_node(head, len):
    curr_node = head

    while curr_node.next:
        curr_node = curr_node.next
    
    return curr_node

def get_new_head_tail(head, loc, len):
    prev = None
    curr_node = head
    i = 0

    while i < loc:
        prev = curr_node
        curr_node = curr_node.next
        i += 1

    if not prev:
        prev = head
        while prev and prev.next:
            prev = prev.next

    return [prev, curr_node]

def get_linked_list_position(l, k):
    position = 0

    if k >= 0:
        position = 0 if (k % l) == 0 else l - (k % l)
    else:
        position = 0 if (-k % l) == 0 else (-k % l)

    return position

def get_length_linked_list(head):
    curr_node = head
    counter = 0

    while curr_node:
        counter += 1
        curr_node = curr_node.next

    return counter 
