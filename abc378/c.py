n = int(input())
a = list(map(int, input().split()))

ans = [-1] * n
last_seen = {}
for i in range(n):
    if a[i] in last_seen:
        ans[i] = last_seen[a[i]] + 1
    last_seen[a[i]] = i  # index starts from 0
print(" ".join(map(str, ans)))

# Before optimization
# ans = [-1] * n
# for i in range(1, n):
#     ans_candi = -1
#     for j in range(i):
#         if a[j] == a[i]:
#             ans_candi = j + 1
#     ans[i] = ans_candi
# print(" ".join(map(str, ans)))
