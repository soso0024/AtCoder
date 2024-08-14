A = []
A += list(map(int, input().split()))
# print(A)
ans = 0
for i in range(len(A)):
    if A[i] == 1:
        ans += 2**i
print(ans)


# Other Solution
A = list(map(int, input().split()))
ans = 0
for i in range(len(A)):
    ans += A[i] * (2**i)

print(ans)
