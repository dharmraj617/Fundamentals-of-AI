a = [12, 45, 67, 4, 89, 2]

n = len(a)

for i in range(n):
    for j in range(0, n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("sorted list:", a)
