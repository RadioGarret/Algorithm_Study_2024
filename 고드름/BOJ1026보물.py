N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A의 최댓값과 B의 최솟값이 곱해지도록 하기
sum_v = 0
while A:
    sum_v += max(A) * min(B)
    A.remove(max(A))
    B.remove(min(B))
print(sum_v)