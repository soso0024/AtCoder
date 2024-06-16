N, L, R = map(int, input().split())
# print(N, L, R)

result = []
for i in range(1, N + 1):
    result.append(i)

result[L - 1 : R] = result[L - 1 : R][
    ::-1
]  # Pythonのリストのスライス（部分取り出し）では、終了インデックスが含まれないため、R - 1にする必要がない

print(" ".join(map(str, result)))
