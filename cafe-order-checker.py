def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # Check if we're serving orders first-come, first-served
    # if severd order is empty but there is atleast one order in the other two lists, return false
    if len(served_orders) == 0 and (len(take_out_orders) != 0 or len(dine_in_orders) != 0):
        return False
    # if any of the two lists have a greater length than served orders, return false
    if len(take_out_orders) > len(served_orders) or len(dine_in_orders) > len(served_orders):
        return False

    # use three pointers for the three lists
    too = 0
    dio = 0
    # loop through the list
    for i in range(len(served_orders)): 
        # check if the element matches the first element in either of the two lists
        order = served_orders[i] 
        if too < len(take_out_orders) and take_out_orders[too] == order: 
            too += 1
        elif dio < len(dine_in_orders) and dine_in_orders[dio] == order: 
            dio += 1 
        else:
            # if it does not, then return false
            return False

    # if the three pointers have a value equal to the length of their list, then return true
    return too == len(take_out_orders) and dio == len(dine_in_orders) and i == len(served_orders) - 1 
