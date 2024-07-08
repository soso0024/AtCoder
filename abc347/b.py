S = input()

ans = []
ans_count = 0
for i in range(len(S)):
    if S[i] not in ans:
        ans.append(S[i])
        ans_count += 1
    s = S[i]
    for j in range(i + 1, len(S)):
        s += S[j]
        if s not in ans:
            ans.append(s)
            ans_count += 1
            # print(ans)

print(ans_count)

# Other Solution
S = input()
L = set() # 
for i in range(len(S)):
    for o in range(i, len(S)):
        L.add(S[i:o+1])
print(len(L))