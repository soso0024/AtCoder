N = int(input())
A = list(map(int, input().split()))


save = 0
ans_count = 0
ans_list = []

for i in range(N):
    while A[i] != i + 1:
        save = A[i]
        A[i] = A[A[i] - 1]
        A[save - 1] = save
        ans_list.append(
            f"{i + 1} {save}"
        )  # 入れ替えた値ではなく，インデックスを表示する

print(len(ans_list))
for i in range(len(ans_list)):
    print(ans_list[i])

# Candi 1
# i = 0
# count = 1
# while i < N:
#     if A[i] == count:
#         # print("Im here")
#         count += 1
#         i += 1
#     else:
#         save = A[i]
#         A[i] = A[A[i] - 1]
#         A[save - 1] = save
#         ans_count += 1
#         ans_list.append(f"{A[i]} {A[save - 1]}")
# print(A)


# Candi 2, Order -> O(N^2)
# ans = 0
# ans_list = []
# save = 0
# for j in range(1, N):
#     for i in range(0, j):
#         if A[j] < A[i] and j > i:
#             ans += 1
#             save = A[j]
#             A[j] = A[i]
#             A[i] = save
#             ans_list.append(f"{A[i]} {A[j]}")
#             # print(f"{A[j]} {A[i]}")

# print(ans)
# for i in range(len(ans_list)):
#     print(ans_list[i])

# print(A)
