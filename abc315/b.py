M = int(input())
D = list(map(int, input().split()))
# print(D)

tol_day = -1
for i in range(M):
    tol_day += D[i]

def_mid_day = (tol_day + 1) / 2
mid_day = (tol_day + 1) / 2
month = 0
for j in range(M):
    mid_day -= D[j]
    if mid_day < 0:
        break
    month += 1

day = 0
for k in range(month):
    day += D[k]
# print(day, mid_day)

cnt = 0
while day < def_mid_day:
    day += 1
    cnt += 1

print(f"{month + 1} {cnt}")

# Other Solution
m = int(input())
d = list(map(int, input().split()))

tot = 0
for x in d:
    tot += x

mid = (tot + 1) // 2

for i in range(m):
    if mid <= d[i]:
        print(str(i + 1) + " " + str(mid))
        exit()
    else:
        mid -= d[i]
