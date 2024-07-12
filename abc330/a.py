N, L = map(int, input().split())
tol = 0
a = list(map(int, input().split()))
for i in range(N):
    if a[i] >= L:
        tol += 1
print(tol)
