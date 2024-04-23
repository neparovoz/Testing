import random

n = int(input())
a = [[random.randint(0, 9) for i in range(n)] for i in range(n)]


for row in a:
    print("".join(map(str, row)))

for j in range(n):
    for k in range(n - 1):
        amin = a[k][j]
        m = k
        for i in range(k + 1, n):
            if a[i][j] < amin:
                amin = a[i][j]
                m = i
        a[m][j], a[k][j] = a[k][j], amin

print("------")
for row in a:
    print("".join(map(str, row)))
