# B를 크기순대로 정렬해서 인덱스를 반환
def solve(array, start, end):
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
        print(f'left:{left},right:{right},pivot:{pivot}')
        print(f'{array[right]},{array[pivot]}')
        array[pivot], array[right] = array[right], array[pivot]
    else:
        print(f'left:{left},right:{right},pivot:{pivot}')
        print(f'{array[right]},{array[pivot]}')
        array[left], array[right] = array[right], array[left]
    solve(array, start, right - 1)
    solve(array, right + 1, end)


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sort_B = B

solve(sort_B, 0, N-1)