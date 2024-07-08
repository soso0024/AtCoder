N, K = map(int, input().split())

A = list(map(int, input().split()))

if len(A) != N:
    print("Exit")
    exit()

box = []
for i in range(N):
    if A[i] % K == 0:
        box.append(A[i])

ans = []
for j in range(len(box)):
    # print(box[j])
    num = box[j] / K
    # print(num)
    ans.append(str(int(num)))

print(" ".join(ans))
