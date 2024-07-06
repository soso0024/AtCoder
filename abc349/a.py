N = int(input())
A = list(map(int, input().split()))

if N - 1 != len(A):
    print("Exit")
    exit()

sum = 0
for i in range(len(A)):
    sum += A[i]

print(-sum)
