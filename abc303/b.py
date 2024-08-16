N, M = map(int, input().split())
a = []
for _ in range(M):
    a.append(list(map(int, input().split())))
# Same as above
# A = [list(map(int, input().split())) for _ in range(M)]

# print(a)
# [[1, 2, 3, 4],
#  [4, 3, 1, 2]]
if N == 2:
    print(0)
    exit()

check = set()
for i in range(M):
    for j in range(N - 1):
        if (a[i][j], a[i][j + 1]) not in check and (a[i][j + 1], a[i][j]) not in check:
            check.add((a[i][j], a[i][j + 1]))
# print(check)
N -= 2  # 初項をインデックス3から１とするための処理
print(int((N**2 + 3 * N + 2) / 2 - len(check)))
