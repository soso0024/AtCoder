s = input()
t = input()

# 両方の文字列の長さの最大値を取得
max_len = max(len(s), len(t))

# 文字列の後半に空白を挿入して長さを揃える
s = s.ljust(max_len)
t = t.ljust(max_len)

for i in range(max_len):
    if s[i] != t[i]:
        print(i + 1)
        exit()

    if s[i] == " " or t[i] == " ":
        break
print(0)
