N = int(input())

# print(N)

for i in range(1, 10):
    for j in range(1, 10):
        # print(i * j)
        if i * j == N:
            print("Yes")
            exit()

print("No")
