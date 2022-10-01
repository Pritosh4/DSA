def search(array, low, high):
  if low <= high:
    mid = (low + high) // 2
    if array[mid] == mid:
      return mid
    result = -1
    if mid + 1 <= array[high]:
      result = search(array, mid + 1, high)
    if result != -1:
      return result
    if mid - 1 >= array[low]:
      return search(array, low, mid - 1)
    
  return -1

array = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
n = len(array)
print("Fixed Point is " + str(search(array, 0, n-1)))
