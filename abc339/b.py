h, w, n = map(int, input().split())
grids = [["." for _ in range(w)] for _ in range(h)]

pos_h, pos_w = 0, 0
direction = 0  # 0: 上, 1: 右, 2: 下, 3: 左

for _ in range(n):
    if grids[pos_h][pos_w] == ".":
        grids[pos_h][pos_w] = "#"
        direction = (direction + 1) % 4  # 時計回りに90度回転
    else:
        grids[pos_h][pos_w] = "."
        direction = (direction - 1) % 4  # 反時計回りに90度回転

    # 移動
    if direction == 0:
        pos_h = (pos_h - 1) % h
    elif direction == 1:
        pos_w = (pos_w + 1) % w
    elif direction == 2:
        pos_h = (pos_h + 1) % h
    else:
        pos_w = (pos_w - 1) % w

# 結果の出力
for row in grids:
    print("".join(row))

# h, w, n = map(int, input().split())
# grids = [list("." * w) for _ in range(h)]
# # print(grids)
# # [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]

# cnt = 0
# pos_h = 0
# pos_w = 0
# direction = 0
# # grids[pos_h][pos_w] = "#"
# # for row in grids:
# #     print("".join(row))

# while cnt <= n - 1:
#     # print(f"Check Value: {grids[pos_h][pos_w]}")
#     if grids[pos_h][pos_w] == ".":
#         grids[pos_h][pos_w] = "#"
#         cnt += 1
#         if cnt % 4 == 1:
#             pos_w += 1
#             if pos_w >= w:
#                 pos_w = 0
#         elif cnt % 4 == 2:
#             pos_h += 1
#             if pos_h >= h:
#                 pos_h = 0
#         elif cnt % 4 == 3:
#             pos_w -= 1
#             if pos_w < 0:
#                 pos_w = w - 1
#         elif cnt % 4 == 0:
#             pos_h -= 1
#             if pos_h < 0:
#                 pos_h = h - 1
#     else:
#         grids[pos_h][pos_w] = "."
#         cnt += 1
#         if cnt % 4 == 1:
#             pos_w -= 1
#             if pos_w < 0:
#                 pos_w = w - 1
#         elif cnt % 4 == 2:
#             pos_h -= 1
#             if pos_h < 0:
#                 pos_h = h - 1
#         elif cnt % 4 == 3:
#             pos_w += 1
#             if pos_w >= w:
#                 pos_w = 0
#         elif cnt % 4 == 0:
#             pos_h += 1
#             if pos_h >= h:
#                 pos_h = 0
#     print(f"POS_H: {pos_h}\nPOS_W: {pos_w}\nCNT: {cnt}")
#     for row in grids:
#         print("".join(row))
#     print()
