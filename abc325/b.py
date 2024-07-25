n = int(input())
cnt = [0 for _ in range(24)]
for i in range(0, n):
    w, x = map(int, input().split())
    cnt[x] += w
# print(cnt)
# [5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0] 時刻 0 ~ 24時間の中で動ける人材の数

ans = 0
for i in range(24):
    sum = 0
    for j in range(9):
        sum += cnt[(i + j) % 24]
    ans = max(ans, sum)

print(ans)

# N = int(input())
# W_X = []
# for _ in range(N):
#     w_x = list(map(int, input().split()))
#     W_X.append(w_x)
# # print(W_X)
# # print(W_X[0][0])
# # [[5, 0], [3, 3], [2, 18]]
# # 5
# sorted_W_X = sorted(W_X, key=lambda x: x[-1])
# print(f"\nsorted: {sorted_W_X}")
#
# tol_person_box = []
# for i in range(N):
#     tol_person = 0
#     print(f"\n------- START i = {i} ------")
#     # tol_person = W_X[i][0]
#     # min_time = W_X[i][1]
#     diff_time = abs(9 - sorted_W_X[i][1])
#     for j in range(i, N, 1):
#         # if abs(sorted_W_X[i][1] - sorted_W_X[j][1]) <= 9:
#         # if sorted_W_X[i][1] >= 9:
#         #     tt = sorted_W_X[j][1] - diff_time
#         # else:
#         #     tt = sorted_W_X[j][1] + diff_time
#
#         if (9 - diff_time) % 24 <= sorted_W_X[j][1] <= (18 - diff_time) % 24:
#             # Debug
#             print(
#                 f"W_X[{i}][1]: {sorted_W_X[i][1]}, W_X[{j}][1]: {sorted_W_X[j][1]}")
#             print(f"ADD!!!{sorted_W_X[j][0]}")
#             # print(f"tt: {tt}")
#             tol_person += sorted_W_X[j][0]
#     tol_person_box.append(tol_person)
#     print(f"------- FIN i = {i} ------\n")
#
# print(tol_person_box)
# print(max(tol_person_box))
