def max_duffel_bag_value(cake_tuples, weight_capacity):
    if weight_capacity == 0:
        return 0

    cache = {}

    for i in range(weight_capacity + 1):
        cache[i] = 0

    for weight in range(weight_capacity + 1): # 4
        max_value_at_weight = 0
        for cake in cake_tuples: # (2, 1) 
            max_value_cake = 0
            if cake[0] == 0 and cake[1] != 0:
                return float('inf')

            if cake[0] <= weight: # 2 <= 4
                max_value_cake = cake[1] # 1
                remaining_weight = weight - cake[0] # 2
                max_value_at_weight = max(max_value_at_weight, max_value_cake + cache[remaining_weight]) # 2

        cache[weight] = max_value_at_weight # {0: 0, 1: 0, 2: 1, 3: 1, 4: 2}

    return cache[weight_capacity] 

