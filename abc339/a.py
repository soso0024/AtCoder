S = input()
# print(f"Len S: {len(S) - 1}")
# print(S.index("."))

reverse_S = S[::-1]
# print(reverse_S)
# print(reverse_S.index("."))

idx = len(S) - 1 - reverse_S.index(".")
# print(idx)

ans = []
for i in range(idx + 1, len(S)):
    ans.append((S[i]))
print("".join(ans))

# Other Solution
S = input()
ans = []

for s in S:
    if s == ".":
        ans = []
    else:
        ans.append(s)

print("".join(ans))
