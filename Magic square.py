def generate_magic_square(n):

    magic_square = [[0 for i in range(n)] for j in range(n)]

    i = 0
    j = n // 2

    for num in range(1, n**2+1):
        magic_square[i][j] = num

        next_i = (i - 1) % n
        next_j = (j + 1) % n

        if magic_square[next_i][next_j] != 0:
            next_i = (i + 1) % n
            next_j = j

        i = next_i
        j = next_j

    return magic_square


magic_square = generate_magic_square(3)


for row in magic_square:
    print(row)
