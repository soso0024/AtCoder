B = int(input())

for i in range(1, 16):  # 15 is minimum
    if i ** i == B:
        print(i)
        exit()
print(-1)
