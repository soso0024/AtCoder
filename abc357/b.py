S = input()

if (len(S) % 2) != 1:
    print("Nooo")
    exit()

even = 0  # 　偶数
odd = 0  # 奇数

for one_chara in S:
    if one_chara.isupper():
        even += 1
    else:
        odd += 1

if even > odd:
    print(S.upper())
else:
    print(S.lower())
