N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))
ans = 0
for i in range(N):
    same_cnt = 0
    for j in range(M):
        if C[i] in D:
            # print("IN!!!")
            if C[i] == D[j]:
                ans += P[j + 1]
                break
        else:
            ans += P[0]
            # print("Im here 2")
            break
print(ans)
