n, c = map(int, input().split())
t = list(map(int, input().split()))

# print(t)

last_time = t[0]
ans = 1

for i in range(1, n):
    if t[i] - last_time >= c:
        ans += 1
        # print("Hi")
        last_time = t[i]

print(ans)
