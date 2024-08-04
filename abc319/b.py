N = int(input())

n = 1
measure = []  # measure is "約数"
while n < 10:
    if N % n == 0:
        measure.append(n)
    n += 1
# print(measure)

ans = []

for i in range(N + 1):
    ok = True
    for j in range(len(measure)):
        temp = N / measure[j]
        if i % temp == 0:
            ans.append(str(measure[j]))
            ok = False
            break
    if ok:
        ans.append("-")
        ok = True

print("".join(ans))
