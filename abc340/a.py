a, b, d = map(int, input().split())

ans = []
for i in range(a, b, d):
    ans.append(str(i))
ans.append(str(b))
print(" ".join(ans))
