array = [7,9,1,3,2,6,8,4,5]

N = len(array)
for i in range(N):
    min_index = i
    for j in range(i + 1, N):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]

print(array)