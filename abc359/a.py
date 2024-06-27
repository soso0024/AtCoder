N = int(input())

S = []

for _ in range(N):
    s = input()
    S.append(s)

ans = 0
for i in range(N):
    if S[i] == "Takahashi":
        ans += 1

print(ans)
