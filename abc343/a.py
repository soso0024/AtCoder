A, B = map(int, input().split())

sum = A + B

for i in range(10):
    if i == sum:
        continue
    print(i)
    exit()
