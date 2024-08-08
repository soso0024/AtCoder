N = int(input())
D = {}

for i in range(N):
    C = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a in D:
            D[a].append((C, i + 1))
        else:
            D[a] = [(C, i + 1)]
# print(D)
# {
#     7: [(3, 1)],
#     19: [(3, 1), (4, 2), (3, 4)],
#     20: [(3, 1)],
#     4: [(4, 2)],
#     24: [(4, 2), (3, 4)],
#     0: [(4, 2)],
#     26: [(2, 3)],
#     10: [(2, 3)],
#     31: [(3, 4)],
# }

X = int(input())
# print(f"D[X]: {D[X]}")
# Case of X = 19
# D[X]: [(3, 1), (4, 2), (3, 4)]

if X in D:
    ans = D[X]
    ans.sort()
    MINC = ans[0][0]
    ans = [x[1] for x in ans if x[0] == MINC]
    # print(f"ANS: {ans}")
    # ANS: [1, 4]
    print(len(ans))
    print(" ".join(map(str, ans)))
else:
    print(0)
    print()
