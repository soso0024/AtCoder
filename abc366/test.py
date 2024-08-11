N = int(input())
S = [input() for _ in range(N)]
M = max(map(len, S))
T = [["*"] * N for _ in range(M)]
print(S)
for i in range(N):
    for j in range(len(S[i])):
        T[j][N - i - 1] = S[i][j]
print(T)
# [["f", "d", "a"], ["g", "e", "b"], ["h", "*", "c"], ["i", "*", "*"]]

# for i in range(M):
#     while T[i][-1] == "*":
#         T[i].pop()
#     print("".join(T[i]))
