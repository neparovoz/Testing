k = int(input("Введите k: "))
N = int(input("Введите N: "))
sum = 0

for i in range(1, N + 1):
    a = 1
    for j in range(1, k + 1):
        a *= i
    sum += a

print("Сумма:", sum)