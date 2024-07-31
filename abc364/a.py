N = int(input())
S = []

for _ in range(N):
    s = input()
    S.append(s)
# print(S)

for i in range(N - 1):
    if S[i] == S[i + 1] == "sweet" and i != N - 2:
        print("No")
        exit()
print("Yes")
