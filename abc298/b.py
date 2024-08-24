N = int(input())
A, B = [], []
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))
# print(A)
# [[0, 1, 1],
#  [1, 0, 0],
#  [0, 1, 0]]
ans = "No"
for cnt in range(4):
    flag = True
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                if B[i][j] != 1:
                    flag = False
    if flag:
        ans = "Yes"
        break

    tmp = A
    A = [[0] * N for _ in range(N)]
    # print(A)
    # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for ni in range(N):
        for nj in range(N):
            A[ni][nj] = tmp[N - 1 - nj][ni]
    # print(A)

print(ans)
