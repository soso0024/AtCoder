N, S, M, L = map(int, input().split())

ans = 10 ** 10
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i * 6 + j * 8 + k * 12 >= N:
                ans = min(ans, (i * S + j * M + k * L))
print(ans)

# Other Solution
n, s, m, l = map(int, input().split())
ans = 10 ** 6
for i1 in range(101):
    for i2 in range(101 - i1):
        for i3 in range(101 - i1 - i2):
            if i1 * 6 + i2 * 8 + i3 * 12 >= n:
                ans = min(ans, i1 * s + i2 * m + i3 * l)

print(ans)
