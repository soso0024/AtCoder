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

# Other Solution
N = int(input())
cnt = 0
while True:
    if N % 2 == 0:
        cnt += 1
        N //= 2
        if N == 0:
            break
    else:
        break
print(cnt)
