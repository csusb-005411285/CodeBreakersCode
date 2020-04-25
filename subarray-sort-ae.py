# tc: o(n), sc: o(1)
def subarraySort(array):
  indices = [-1, -1] #1
  smallest_element = float('inf') #1
  largest_element = float('-inf') #1

  for i in range(len(array)): #n
    if is_out_of_order(i, array):
      smallest_element = min(smallest_element, array[i])
      largest_element = max(largest_element, array[i])

  if smallest_element == float('inf') or largest_element == float('-inf'):
    return [-1, -1 ]

  j = 0
  while array[j] <= smallest_element: #n 
    j += 1 
  indices = [j]

  k = len(array) - 1 
  while largest_element <= array[k]: #n 
    k -= 1
  indices.append(k)
  
  return indices

def is_out_of_order(i, array):
  if i == 0:
    return array[i] > array[i + 1] #
  if i == len(array) - 1:
    return array[i] < array[i - 1] #
  else:
    return array[i - 1] > array[i] or array[i] > array[i + 1] 
