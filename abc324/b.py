N = int(input())
n = 0
while n < N:
    for i in range(10 ** 2):
        for j in range(10 ** 2):
            n = 2 ** i * 3 ** j
            if n == N:
                print("Yes")
                exit()
print("No")
