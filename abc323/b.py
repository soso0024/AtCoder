N = int(input())
S = []
o_cnt_dic = {}
ans = []

for i in range(N):
    s = input().strip()  # delete unnecessary blank space
    S.append(s)
    o_cnt = s.count('o')
    o_cnt_dic[i] = o_cnt
# print(S)
# print(o_cnt_dic)

dic2 = sorted(o_cnt_dic.items(), key=lambda x: x[1], reverse=True)
for i in range(N):
    # print(str(dic2[i][0] + 1))
    ans.append(str(dic2[i][0] + 1))

print(" ".join(ans))
