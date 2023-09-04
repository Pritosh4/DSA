9def minmax(array, start, end):
    # If only 1 element in the array
    if start == end:
        return (array[start], array[end])
    # If only 2 elements in the array
    elif start + 1 == end:
        if array[start] > array[end]:
            return (array[end], array[start])
        else:
            return (array[start], array[end])
    # More than 2 elements in the array
    else:
        mid = (start + end) // 2
        arr_minl, arr_maxl = minmax(array, start, mid)
        arr_minr, arr_maxr = minmax(array, mid+1, end)
        return (min(arr_minl, arr_minr), max(arr_maxl, arr_maxr))

array = [1000, 11, 445, 1, 330, 3000]
end = len(array) - 1
start = 0
arr_min, arr_max = minmax(array, start, end)
print('Minimum element is ', arr_min)
print('Maximum element is ', arr_max)