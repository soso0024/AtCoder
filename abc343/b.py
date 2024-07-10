N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
# print(A)
ans = []
for i in range(N):
    row = []
    for j in range(N):
        if A[i][j] == 1:
            row.append(str(j + 1))
    # print(row)
    ans.append(" ".join(row))
    # print(ans)
print("\n".join(ans))

# Other Solution
N = int(input())
A = [[int(x) for x in input().split()] for i in range(N)]

for i in range(N):
    B = []
    for j in range(N):
        if A[i][j] == 1:
            B.append(j + 1)
    print(*B)
