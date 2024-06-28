N = int(input())
A = list(map(int, input().split()))

for i in range(len(A)):
    if A[i] > N:
        print("Exit")
        exit()

ans = 0
for i in range(0, len(A) - 2):
    if A[i] == A[i + 2]:
        ans += 1

print(ans)
