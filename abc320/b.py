S = input()
# print(S[1])
ans = 0
for i in range(len(S)):
    for j in range(len(S) - i):
        A = S[j:i + j + 1:]
        B = A[::-1]
        if A == B:
            ans = max(ans, i + 1)
print(ans)
