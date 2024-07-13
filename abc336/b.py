n = int(input())
binary_n = bin(n)[2:]
# print(binary_n)
# print(len(binary_n))

if binary_n[-1] != str(0):
    print(0)
    exit()

cnt = 0
for i in range(len(binary_n) - 1, 0, -1):
    # print(binary_n[i])
    if binary_n[i] == str(0):
        # print("Im here")
        cnt += 1
    else:
        break

print(cnt)
