N = int(input())
A = list(map(int, input().split()))
# print(A)

sorted_A = sorted(A)
# print(sorted_A)
ans = -1
for i in range(len(sorted_A) - 1):
    if sorted_A[i] + 1 != sorted_A[i + 1]:
        ans = sorted_A[i] + 1
        break
print(ans)
