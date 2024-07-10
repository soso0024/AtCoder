S = input()

for i in range(len(S) - 2):
    if S[i] != S[i + 1]:
        if S[i] == S[i + 2]:
            print(i + 2)
            exit()
        elif S[i + 1] == S[i + 2]:
            print(i + 1)
            exit()

if S[0] != S[-1]:
    print(len(S))
    exit()

# Other Solution
from collections import defaultdict

d = defaultdict(int)

s = input()
for c in s:
    d[c] += 1

index = 0
for c, n in d.items():
    if n == 1:
        index = s.find(c)

print(index + 1)
