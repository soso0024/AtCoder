N = int(input())

H = list(map(int, input().split()))

if N != len(H):
    print("Exit !!!")
    exit()

max_val = H[0]
index = 1
max_index = 0
for index in range(N):
    if max_val < H[index]:
        max_val = H[index]
        max_index = index + 1
        break

if max_index == 0:
    print("-1")
else:
    print(max_index)
