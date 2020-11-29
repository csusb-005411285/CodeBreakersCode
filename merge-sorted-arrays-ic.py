def merge_lists(my_list, alices_list):
    if not my_list and not alices_list: return []
    if not my_list: return alices_list
    if not alices_list: return my_list
    ml = 0
    al = 0
    res = []
    while ml < len(my_list) and al < len(alices_list):
        if my_list[ml] < alices_list[al]:
            res.append(my_list[ml])
            ml += 1
        else:
            res.append(alices_list[al])
            al += 1
    if ml < len(my_list):
        res = res + my_list[ml:]
    elif al < len(alices_list):
        res = res + alices_list[al:]
    return res
   
