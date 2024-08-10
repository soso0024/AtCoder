N, M = map(int, input().split())
P, C, F = [], [], []
for _ in range(N):
    tmp = list(map(str, input().split()))
    P.append(tmp[0])
    C.append(tmp[1])
    F.append(tmp[2:])
# print(F)
# [['1', '3'],
# ['1', '2', '4'],
# ['1', '3', '5'],
# ['1', '5'],
# ['1', '2', '3', '4', '5', '6']]
ans = False
for i in range(N):
    for j in range(i + 1, N):
        if all(element in F[j] for element in F[i]):
            if P[i] == P[j] and C[i] > C[j]:
                ans = True
                # print(f"P[i]: {P[i]}, P[j]: {P[j]}")
                break
            if P[i] > P[j]:
                ans = True
                # print(f"P[i]: {P[i]}, P[j]: {P[j]}")
                break

        if all(element in F[i] for element in F[j]):
            if P[i] == P[j] and C[i] < C[j]:
                ans = True
                # print(f"P[i]: {P[i]}, P[j]: {P[j]}")
                break
            if P[i] < P[j]:
                ans = True
                # print(f"P[i]: {P[i]}, P[j]: {P[j]}")
                break
if ans:
    print("Yes")
else:
    print("No")

# Memo
# A = [1, 3]
# B = [1, 2, 3, 5]
# if all(element in B for element in A):
#     print("Monger!")
# else:
#     print("Hi")
