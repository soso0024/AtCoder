N = int(input())
A = []
for _ in range(N):
    A.append(list(input()))
# print(A)
# ans = A
ans = [row[:] for row in A]  # ここ重要
# print(ans)
for i in range(N):
    for j in range(N - 1):
        if i == 0:
            ans[i][j + 1] = A[i][j]

        if i == N - 1:
            ans[i][j] = A[i][j + 1]
        else:
            if j == N - 2:
                ans[i + 1][-1] = A[i][-1]

            if j == 0 and i != N - 1:
                ans[i][j] = A[i + 1][0]
# print()
for i in range(N):
    print("".join(ans[i]))
