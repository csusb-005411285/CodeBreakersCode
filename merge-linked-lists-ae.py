# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# tc: o(n), sc:
def mergeLinkedLists(headOne, headTwo):
    '''
    solve only the failing test cases
    '''
    p1 = headOne
    p2 = headTwo
    prev = None

    while p1 and p2:
        if p1.value < p2.value:
            prev = p1
            p1 = p1.next
        else:
            temp_p2 = p2.next
            p2.next = p1

            if prev:
                prev.next = p2
                prev = prev.next
            else:
                prev = p2

            p2 = temp_p2

    if p2:
        prev.next = p2
    
    return headOne if headOne.value < headTwo.value else headTwo   
