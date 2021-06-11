def find_min_fee(fee):
  return _find_min_fee(fee, 0)

def _find_min_fee(fee, i):
  n = len(fee)
  if i >= n:
    return 0
  fee1 = fee[i] + _find_min_fee(fee, i + 1)
  fee2 = fee[i] + _find_min_fee(fee, i + 2)
  fee3 = fee[i] + _find_min_fee(fee, i + 3)
  return min(fee1, fee2, fee3)


def find_min_fee(fee):
  cache = [0 for _ in range(len(fee) + 1)]
  cache[1] = fee[0]
  cache[2] = fee[0]
  for i, val in enumerate(cache[3:], start=3):
    cache[i] = min(cache[i - 1] + fee[i - 1], cache[i - 2] + fee[i - 2], cache[i - 3] + fee[i - 3])
  return cache[-1]
 
