n, d = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
# print(s)
# ['xooox', 'oooxx', 'oooxo']
tmp = []
for j in range(d):
    ok = True
    for i in range(n):
        if s[i][j] == "x":
            ok = False
    if ok:
        tmp += "o"
    else:
        tmp += "x"
# print(tmp)
a = 0
ans = 0
for i in range(d):
    if tmp[i] == "o":
        a += 1
    else:
        a = 0
    ans = max(ans, a)
print(ans)
