N, M = map(int, input().split())
H = input().split()

if N != len(H):
    print("Nooooo")
    exit()

# print(N, M)
# print(H)
heal = 0
count = 0

for i in range(N):
    heal += int(H[i])

    if heal <= M:
        count += 1
        # print(heal)

print(count)
