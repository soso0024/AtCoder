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


# Other Solution
def find(Str, List):
    if Str in List:
        return List.index(Str) + 1
    else:
        return 0


N, M = map(int, input().split())
C = [s for s in input().split()]
D = [s for s in input().split()]
P = [int(num) for num in input().split()]

ans = 0
for n in range(N):
    ans += P[find(C[n], D)]

print(ans)
