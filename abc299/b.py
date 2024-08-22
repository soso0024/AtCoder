N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
# print(C)
in_T = False
max_val = -1
max_idx = -1
for i in range(N):
    if T == C[i]:
        if max_val < R[i]:
            max_val = R[i]
            max_idx = i
        in_T = True

if in_T == False:
    # print("Im here")
    for i in range(N):
        if max_val < R[i] and C[0] == C[i]:
            max_val = R[i]
            max_idx = i

print(max_idx + 1)
