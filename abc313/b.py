N, M = map(int, input().split())
info_strength = []
for _ in range(M):
    info_strength.append(list(map(int, input().split())))
# print(info_strength)

s = [0] * N
# print(s)
for i in range(M):
    s[info_strength[i][1] - 1] += 1
# print(s)
cnt = 0
No1 = -1
for i in range(len(s)):
    if s[i] == 0:
        cnt += 1
        No1 = i + 1
if cnt == 1:
    print(No1)
else:
    print(-1)
