def find_max_steal(wealth):
  return _find_max_steal(wealth, len(wealth) - 1)

def _find_max_steal(wealth, i):
  if i < 2:
    return wealth[i]
  return max(_find_max_steal(wealth, i - 2) + wealth[i], _find_max_steal(wealth, i - 1))


def find_max_steal(wealth):
  cache = [0 for _ in range(len(wealth))]
  cache[0] = wealth[0]
  cache[1] = wealth[1]
  for i in range(2, len(cache)):
    cache[i] = max(cache[i - 2] + wealth[i], cache[i - 1])
  return cache[-1]
