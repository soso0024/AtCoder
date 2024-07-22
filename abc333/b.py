S = list(input())
s1, s2 = S[0], S[-1]
T = input()
t1, t2 = T[0], T[-1]
# print(t2)

# 文字と数字のマッピングを作成
char_to_num = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

# s1, s2, t1, t2 に対応する数字を取得
s1_num = char_to_num[s1]
s2_num = char_to_num[s2]
t1_num = char_to_num[t1]
t2_num = char_to_num[t2]

# print(f"{s1}={s1_num}, {s2}={s2_num}")
# print(f"{t1}={t1_num}, {t2}={t2_num}")

if abs(s2_num - s1_num) == 4:
    s2_s1 = 1
else:
    s2_s1 = abs(s2_num - s1_num)
if abs(t2_num - t1_num) == 4:
    t2_t1 = 1
else:
    t2_t1 = abs(t2_num - t1_num)
# print(s2_s1, t2_t1)

if s2_s1 == t2_t1 or (s2_s1 == 3 and t2_t1 == 4) or (
        s2_s1 == 4 and t2_t1 == 3) or (s2_s1 == 3 and t2_t1 == 2) or (
        s2_s1 == 2 and t2_t1 == 3):
    print("Yes")
else:
    print("No")
