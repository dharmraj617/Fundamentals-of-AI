A = [[5, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print("Matrix addition:")
for row in C:
    print(row)

C = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] - B[i][j])
    C.append(row)
print("Matrix subtraction:")
for row in C:
    print(row)

C = []
for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        s = 0
        for k in range(len(B)):
            s += A[i][k] * B[k][j]
        row.append(s)
    C.append(row)
print("Matrix multiplication:")
for row in C:
    print(row)
