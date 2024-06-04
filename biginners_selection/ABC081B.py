num = int(input())
# print("num: " + str(num))

list = [int(i) for i in input().split()]

if num != len(list):
    # print("len(list): " + str(len(list)))
    print("error")
    exit()

# print(list)

count = 0
while True:
    for i in range(num):
        if list[i] % 2 == 1:
            print(count)
            exit()
        list[i] = list[i] / 2
    count += 1
