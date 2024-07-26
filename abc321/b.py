N, X = map(int, input().split())
A = list(map(int, input().split()))
sorted_A = sorted(A)
# print(sorted_A)

low = sorted_A.pop(0)
print(f"low: {low}")
high = sorted_A.pop()
print(f"high: {high}")
print(sorted_A)

tol = 0
for i in range(len(sorted_A)):
    tol += sorted_A[i]

if N == 3:
    if low < X < high:
        print(X)
        exit()
    elif X == low and X == high:
        print(0)
        exit()
    elif X == low:
        print(low)
        exit()
    elif X == high:
        print(high)
        exit()

if tol + high < X:
    print(-1)
    print("Im here 1")
    exit()

if tol - low > X:
    print(0)
    print("Im here 2")
    exit()

if low == high:
    print(0)
    exit()

if X - tol <= low:
    print(0)
else:
    print(X - tol)


# Other Solution
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(101):
    b = a.copy()
    b.append(i)
    b.sort()
    if sum(b[1 : n - 1]) >= x:
        print(i)
        exit()

print(-1)

# Other Solution 2
N, X = map(int, input().split())
A = list(map(int, input().split()))
A.append(-1)

for last in range(0, 101):
    B = A.copy()
    B[N - 1] = last
    sum = 0
    ma = 0
    mi = 100
    for p in B:
        sum += p
        ma = max(ma, p)
        mi = min(mi, p)
    score = sum - ma - mi

    if score >= X:
        print(last)
        exit()

print("-1")
