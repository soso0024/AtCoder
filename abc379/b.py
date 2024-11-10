n, k = map(int, input().split())
s = input()

count = 0
can_eat = 0
for teeth in s:
    if teeth == "O":
        count += 1
    else:
        count = 0

    if count == k:
        can_eat += 1
        count = 0

print(can_eat)
