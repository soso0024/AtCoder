n, m = map(int, input().split())
coordinates = set(tuple(map(int, input().split())) for _ in range(m))

coord_list = list(coordinates)
# for i in range(m):
#     print("座標:", coord_list[i])

# リストの代わりにsetを使用
a = set()
for i in range(m):
    a.add((coord_list[i][0] - 1, coord_list[i][1] - 1))

    if coord_list[i][0] - 1 + 2 < n and coord_list[i][1] - 1 + 1 < n:
        # 座標をタプルとしてsetに追加
        a.add((coord_list[i][0] - 1 + 2, coord_list[i][1] - 1 + 1))

    if coord_list[i][0] - 1 + 1 < n and coord_list[i][1] - 1 + 2 < n:
        a.add((coord_list[i][0] - 1 + 1, coord_list[i][1] - 1 + 2))

    if coord_list[i][0] - 1 - 1 > -1 and coord_list[i][1] - 1 + 2 < n:
        a.add((coord_list[i][0] - 1 - 1, coord_list[i][1] - 1 + 2))

    if coord_list[i][0] - 1 - 2 > -1 and coord_list[i][1] - 1 + 1 < n:
        a.add((coord_list[i][0] - 1 - 2, coord_list[i][1] - 1 + 1))

    if coord_list[i][0] - 1 - 2 > -1 and coord_list[i][1] - 1 - 1 > -1:
        a.add((coord_list[i][0] - 1 - 2, coord_list[i][1] - 1 - 1))

    if coord_list[i][0] - 1 - 1 > -1 and coord_list[i][1] - 1 - 2 > -1:
        a.add((coord_list[i][0] - 1 - 1, coord_list[i][1] - 1 - 2))

    if coord_list[i][0] - 1 + 1 < n and coord_list[i][1] - 1 - 2 > -1:
        a.add((coord_list[i][0] - 1 + 1, coord_list[i][1] - 1 - 2))

    if coord_list[i][0] - 1 + 2 < n and coord_list[i][1] - 1 - 1 > -1:
        a.add((coord_list[i][0] - 1 + 2, coord_list[i][1] - 1 - 1))

# print("a:", a)
print(n * n - len(a))


# # 方法2: forループで取得
# for coord in coordinates:
#     print("座標:", coord)
