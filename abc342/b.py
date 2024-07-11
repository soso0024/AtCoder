N = int(input())
P = list(map(int, input().split()))
Q = int(input())
A, B = [], []
for _ in range(Q):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

for i in range(Q):
    if P.index(A[i]) < P.index(B[i]):
        print(A[i])
    else:
        print(B[i])
