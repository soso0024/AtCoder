def check(i, j):
    for ii in range(3):
        for jj in range(3):
            if S[i + ii][j + jj] != "#":
                return False

    for ii in range(6, 9, 1):
        for jj in range(6, 9, 1):
            if S[i + ii][j + jj] != "#":
                return False

    for ii in range(4):
        if S[i + ii][j + 3] != ".":
            return False

    for jj in range(4):
        if S[i + 3][j + jj] != ".":
            return False

    for jj in range(5, 9, 1):
        if S[i + 5][j + jj] != ".":
            return False

    for ii in range(5, 9, 1):
        if S[i + jj][j + 5] != ".":
            return False

    return True


N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())
# print(S)
# [
#     "###......###......",
#     "###......###......",
#     "###..#...###..#...",
#     "..............#...",
#     "..................",
#     "..................",
#     "......###......###",
#     "......###......###",
#     "......###......###",
#     ".###..............",
#     ".###......##......",
#     ".###..............",
#     "............###...",
#     "...##.......###...",
#     "...##.......###...",
#     ".......###........",
#     ".......###........",
#     ".......###........",
#     "........#.........",
# ]

for i in range(N - 8):
    for j in range(M - 8):
        if check(i, j):
            print(f"{i + 1} {j + 1}")
