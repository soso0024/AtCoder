A = list(map(int, input().split()))
B = list(map(int, input().split()))

tol_a = 0
tol_b = 0

# print(f"Length of B: {len(B)}")

for i in range(len(A)):
    tol_a += A[i]
    if i < len(B):
        tol_b += B[i]

result = tol_a - tol_b + 1
print(result)
