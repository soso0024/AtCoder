s = input()
x = [0] * 26

for i in range(26):
    x[ord(s[i]) - ord("A")] = i

ans = 0
for j in range(25):
    ans += abs(x[j] - x[j + 1])

print(ans)

# Other solution
s = input()
a = 0
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(s) - 1):
    a += abs(s.index(s2[i]) - s.index(s2[i + 1]))
print(a)
