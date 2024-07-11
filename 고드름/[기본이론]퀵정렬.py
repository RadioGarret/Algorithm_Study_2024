array = [5,7,9,0,3,1,6,2,4,8]


def quick_sort(array, start, end):
    if start == end:
        return
    pivot = start
    left = start + 1
    right = end
    while array[pivot] < array[left]:
        left += 1
    while array[pivot] > array[right]:
        right -= 1
    if left > right:
        array[pivot], array[right] = array[right], array[pivot]
    else:
        array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


N = len(array)
quick_sort(array, 0, N-1)