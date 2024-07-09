N = int(input())
points = []
for i in range(N):
    point_i = tuple(map(int, input().split()))
    points.append(point_i)
sorted_points = sorted(points)
for point in sorted_points:
    x, y = point[0], point[1]
    print(x, end=' ')
    print(y)