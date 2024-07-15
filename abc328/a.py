n, x = map(int, input().split())
S = []
s = map(int, input().split())
S += s
# print(S)
ans = 0
for i in range(n):
    if S[i] <= x:
        ans += S[i]

print(ans)
