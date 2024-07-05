# Solution 1 # 113112/112ms
dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))
dwarfs.sort()
diff = sum(dwarfs) - 100
i = 0
j = 8
while i < j:
    if diff > dwarfs[i] + dwarfs[j]:
        i += 1
    elif diff < dwarfs[i] + dwarfs[j]:
        j -= 1
    else:
        break

for k in range(9):
    if k != i and k != j:
        print(dwarfs[k])

# Solution 2 # 30860/76ms
dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))
dwarfs.sort()
total = sum(dwarfs)

for i in range(len(dwarfs)):
    for j in range(i+1, len(dwarfs)):
        if (total - dwarfs[i] - dwarfs[j]) == 100:
            for k in range(len(dwarfs)):
                if k != i and k != j:
                    print(dwarfs[k])
            exit()
        
# Solution 3 # 31256/40ms        
from itertools import combinations

dwarfs = []

for i in range(9):
    dwarfs.append(int(input()))

for com in combinations(dwarfs, 7):
    if (sum(com) == 100):
        for i in sorted(com):
            print(i)
        break
