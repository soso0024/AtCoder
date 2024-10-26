from copy import deepcopy

N = int(input())
A = []
for _ in range(N):
    row = list(input().strip())
    A.append(row)

# B = A.copy()

for i in range(1, N // 2 + 1):
    B = deepcopy(A)

    for x in range(i - 1, N + 1 - i):
        for y in range(i - 1, N + 1 - i):
            # print(x, y)
            B[y][N + 1 - x - 2] = A[x][y]

    A = B
    # print(A)

for row in B:
    print(*row, sep="")
