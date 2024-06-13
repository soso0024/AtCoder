S = input()
# print(len(S))
new_S = S

for _ in range(6):
    if len(new_S) <= 5:
        new_S += S
        # print(new_S)
    elif len(new_S) == 6:
        print(new_S)
        exit()
    else:
        exit()
