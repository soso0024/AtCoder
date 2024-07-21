N, T, P = map(int, input().split())
L = list(map(int, input().split()))

if len(L) != N:
    print("Exit")
    exit()

sorted_L = sorted(L)
target_idx = len(sorted_L) - P
if T - sorted_L[target_idx] < 0:
    print(0)
else:
    print(T - sorted_L[target_idx])

# Other Solution
n, t, p = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
print(max(0, t - l[p - 1]))

# My First Code
# There were TLE & WA.
# ---------------------
# cnt_day = 0
# cnt_guys = 0
# for i in range(len(sorted_L) - 1, -1, -1):
#     if sorted_L[i] >= T:
#         cnt_guys += 1
# # print(cnt_guys)
# if cnt_guys >= P:
#     print(0)
#     exit()
#
# while cnt_guys <= P:
#     cnt_guys = 0
#     cnt_day += 1
#     for i in range(len(sorted_L) - 1, 0, -1):
#         if sorted_L[i] + cnt_day >= T:
#             cnt_guys += 1
# print(cnt_day - 1)
