s = input()
x = [0] * 26
for i in range(26):
    x[ord(s[i]) - ord("A")] = i  # ord("A") = 65, ord("B") = 66, ...
    print(x)
ans = 0
for i in range(25):
    ans += abs(x[i] - x[i + 1])
print(ans)
