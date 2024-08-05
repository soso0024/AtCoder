n = int(input())
grid = [[False for i in range(100)] for i in range(100)]

for k in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a, b):
        for j in range(c, d):
            grid[i][j] = True

ans = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] == True:
            ans += 1
print(ans)
