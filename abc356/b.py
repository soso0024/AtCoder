N, M = map(int, input().split())
A = list(map(int, input().split()))

if M != len(A):
    print("M != len(A)")
    exit()

nutris = []
for _ in range(N):
    nutri = list(map(int, input().split()))
    nutris.append(nutri)
# print(f"\n{nutris}")

tol_box = [0] * M

for i in range(N):
    for j in range(M):
        tol_box[j] += nutris[i][j]
# print(tol_box)

count = 0
for j in range(M):
    if tol_box[j] >= A[j]:
        count += 1

if count == M:
    print("Yes")
else:
    print("No")


# 2 3
# 10 20 30
# 20 0 10
# 0 100 100

# [[20, 0, 10], [0, 100, 100]]

# tol_box = [20, 100, 110, 30]
