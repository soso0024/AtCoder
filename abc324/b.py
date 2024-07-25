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

# Other Solution
N = int(input())

while N % 2 == 0:
    N //= 2

while N % 3 == 0:
    N //= 3

if N == 1:
    print('Yes')
else:
    print('No')
