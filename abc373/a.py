i = 1
ans = 0
for _ in range(12):
    S = input()
    if i == len(S):
        ans += 1
    i += 1

print(ans)
