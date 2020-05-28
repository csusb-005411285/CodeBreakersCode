# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# tc: o(n), sc:
def mergeLinkedLists(headOne, headTwo):
    l1 = headOne
    l2 = headTwo
    
    if not l1 and not l2:
        return l1
    
    if not l1:
        return l2
    
    if not l2:
        return l1
    
    p1 = l1
    p2 = l2
    prev = None

    while p1 and p2:
        if p2.value <= p1.value:
            if not prev:
                prev = p2
            else:
                prev.next = p2
                prev = prev.next
                
            temp_p2 = p2.next
            p2.next = p1
            p2 = temp_p2
        else:
            prev = p1
            p1 = p1.next

    if p2:
        if p2.value <= prev.value:
            p2.next = prev
        else:
            prev.next = p2
        

    return l1 if l1.value < l2.value else l2
