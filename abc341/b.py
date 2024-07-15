n = int(input())
a = list(map(int, input().split()))
s, t = [], []
for _ in range(n - 1):
    i, j = map(int, input().split())
    s.append(i)
    t.append(j)

cnt = 0
for i in range(n - 1):
    cnt = a[i] // s[i]
    a[i + 1] += cnt * t[i]
print(a[-1])
