N = int(input())
w = list(map(int, input().split()))
 
a = sorted(w)
b = sorted(w, reverse=True)
 
arr = []
 
for i in range(len(w)):
    x = a[i] + b[i]
    arr.append(x)
    
print(min(arr))
