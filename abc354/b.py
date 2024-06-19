N = int(input())

all = []
for _ in range(N):
    t = list(map(str, input().split()))
    all.append(t)

# print(all)

names = []
total = 0
for i in range(N):
    names.append(all[i][0])
    total += int(all[i][1])

sorted_names = sorted(names)

mod = total % N
# print(mod, names)

print(sorted_names[mod])

# print(sorted(names))
# print(total)
