s = []
for _ in range(8):
    s.append(input())

i_box = set()  # リストの代わりにsetを使用
j_box = set()  # リストの代わりにsetを使用
for i in range(8):
    for j in range(8):
        if s[i][j] == "#":
            i_box.add(i)  # appendの代わりにaddを使用
            j_box.add(j)  # appendの代わりにaddを使用

# print(i_box, j_box)

remain_i = 8 - len(i_box)
remain_j = 8 - len(j_box)

print(remain_i * remain_j)
