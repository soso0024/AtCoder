N, K = map(int, input().split())
A = list(map(str, input().split()))
# print(A)
for i in range(K):
    A.insert(0, str(A.pop()))
print(" ".join(A))
