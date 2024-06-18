N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(A)

if N != len(A) or M != len(B):
    print("Exit")
    exit()

prev_i = 0
for i in range(N):
    if prev_i == A[i]:
        print("Duplicate A")
        exit()
    prev_i = A[i]

prev_j = 0
for j in range(M):
    if prev_j == B[j]:
        print("Duplicate B")
        exit()
    prev_j = B[j]

C = A + B
# print(C)
C_sorted = sorted(C)
# print(C_sorted)

# pre = 1
# A_sorted = sorted(A)
# for k in range(N):
#     if pre - A_sorted[k] == -1:
#         # print(pre - A_sorted[k])
#         print("Yes")
#         exit()

#     pre = A_sorted[k]

i = 0
while i < len(C_sorted) - 1:
    if C_sorted[i] in A and C_sorted[i + 1] in A:
        print("Yes")
        exit()
    i += 1

print("No")
