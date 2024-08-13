N = int(input())
S, ns = [], []
for _ in range(N):
    S.append(input())
# print(S)
ans = "No"
for i in range(N):
    for j in range(N):
        if S[i] != S[j]:
            ns.append(S[i] + S[j])
# print(ns)
for i in range(len(ns)):
    cnt = 0
    for j in range(len(ns[i])):
        if ns[i][j] == ns[i][len(ns[i]) - 1 - j]:
            cnt += 1
    if cnt == len(ns[i]):
        ans = "Yes"
        break
print(ans)

# Another Solution
n = int(input())
S = []
for _ in range(n):
    S.append(input())

for i in range(n):
    for j in range(n):
        if i != j:
            judge = ""
            judge += S[i]
            judge += S[j]
            if judge == judge[::-1]:
                # list[<start>:<stop>:<step>]
                # Example
                # >>> a = '1234'
                # >>> a[::-1]
                # '4321'
                print("Yes")
                exit()
print("No")

# Official
n = int(input())
s = [input() for i in range(n)]
ans = "No"

for i in range(n):
    for j in range(n):
        if i != j:
            t = s[i] + s[j]
            flag = True
            for k in range(len(t)):
                if t[k] != t[-k - 1]:
                    flag = False
            if flag:
                ans = "Yes"

print(ans)
