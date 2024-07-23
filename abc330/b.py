N, L, R = map(int, input().split())
A = list(map(int, input().split()))
# print(A)
ans = []
for i in range(N):
    prev = 10 * 10
    ans_val = 0
    for j in range(L, R + 1):
        if A[i] <= L:
            ans_val = L
            print("Hi 1")
            break

        if R <= A[i]:
            ans_val = R
            print("Hi 2")
            break

        if L < A[i] < R and L < A[i] < R:
            ans_val = A[i]
            print("Hi 3")
            break
    ans.append(str(ans_val))
print(" ".join(ans))

# Other Solution
N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    if A[i] < L:
        ans.append(L)
    elif A[i] > R:
        ans.append(R)
    else:
        ans.append(A[i])

# 出力
print(*ans)
