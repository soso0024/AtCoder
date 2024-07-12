n, s, k = map(int, input().split())
tol = 0
for _ in range(n):
    p, q = map(int, input().split())
    tol += p * q
if tol >= s:
    print(tol)
else:
    print(tol + k)
