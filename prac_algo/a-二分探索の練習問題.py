N, K = map(int, input().split())

A = list(map(int, input().split()))
# print(A)

flag = False

left = 0
right = N

while (right - left) > 1:
    mid = (right + left) // 2
    # print(mid)
    if A[mid] >= K:
        right = mid
        flag = True
    else:
        left = mid

print(right if flag else -1)

# ans = 0
# for i in range(len(A)):
#     if A[i] >= K:
#         ans = i
#         break
# if ans != 0:
#     print(ans)
# else:
#     print(-1)
