N, K, X = map(int, input().split())
A = list(map(int, input().split()))

if N != len(A):
    print("Exit")
    exit()

ans = []
for i in range(N):
    ans.append(str(A[i]))
    if i + 1 == K:
        ans.append(str(X))

print(" ".join(ans))
