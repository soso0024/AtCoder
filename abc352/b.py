S = list(map(str, input()))
T = list(map(str, input()))

result = []

check_index = 0
for i in range(len(T)):
    check_now_chara = S[check_index]
    if check_now_chara == T[i]:
        check_index += 1
        result.append(i + 1)

print(" ".join(map(str, result)))
