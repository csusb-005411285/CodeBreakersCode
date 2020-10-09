def minNumberOfCoinsForChange(n, denoms):
    if not denoms:
        return -1
    
    if n == 0:
        return 0

    cache = [float('inf') for i in range(n + 1)]
    cache[0] = 0

    for denom in denoms:
        for amt in range(n + 1):
            if amt >= denom:
                if cache[amt - denom] >= 0:
                    cache[amt] = min(cache[amt], 1 + cache[amt - denom]) 

    return cache[n] if cache[n] != float('inf') else -1
