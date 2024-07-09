S = input()

ans = []
cnt = 0
point_one = 0
point_two = 0
for i in range(len(S)):
    if S[i] == "|" and cnt == 0:
        point_one = i
        cnt += 1
    elif S[i] == "|" and cnt == 1:
        point_two = i

ans.append(S[0:point_one] + S[point_two + 1:])
print("".join(ans))

# Other Solution but it takes times
s = input()
ans = s.split('|')
print(ans[0] + ans[2])
