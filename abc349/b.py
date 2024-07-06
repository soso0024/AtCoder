from collections import Counter

S = input()

if len(set(S)) % 2 != 0:  # setは重複しない要素の集まりを求める
    print("No")
    exit()

counts = Counter(S)
# print(counts)
# print(len(counts))

i = 1
while i <= len(counts):
    num = 0
    for element, count in counts.items():
        # print(f"'{element}' : {count}回")
        if i == count:
            num += 1

    i += 1

    if num == 0 or num == 2:
        continue
    else:
        print("No")
        exit()
print("Yes")


# Other Solution
S = input()
S_2 = list(set(S))

cnt = []
for i in range(len(S_2)):
    cnt.append(S.count(S_2[i]))

ans = "Yes"
for j in range(len(S) + 1):
    if cnt.count(j) == 1 or cnt.count(j) > 2:
        ans = "No"

print(ans)
