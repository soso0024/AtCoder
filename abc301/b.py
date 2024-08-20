input()
A = list(map(int, input().split()))
B = []

for i in range(len(A) - 1):
    if A[i] <= A[i + 1]:
        B += list(range(A[i], A[i + 1]))
    elif A[i] > A[i + 1]:
        B += list(range(A[i], A[i + 1], -1))

B.append(A[-1])
print(*B)
