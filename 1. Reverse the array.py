def reverse(array, start, end):
  if start >= end:
    return 
  array[start], array[end] = array[end], array[start]
  return reverse(array, start+1, end-1)

array = [1, 2, 3, 4, 5, 6]
print(array)
reverseList(array, 0, len(array)-1)
print("Reversed list is")
print(A)
