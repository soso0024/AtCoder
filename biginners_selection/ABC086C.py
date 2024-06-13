N = int(input())
schedules = []

for i in range(N):
    schedule = list(map(int, input().split()))
    # print(schedule)
    schedules.append(schedule)

# print(schedules)

# N = 2
# 2 4 5
# [2, 4, 5]

# 3 5 6
# [3, 5, 6]

# [[2, 4, 5], [3, 5, 6]]


def check(current, destination):
    step = destination[0] - current[0]
    dis_x = abs(destination[1] - current[1])
    dis_y = abs(destination[2] - current[2])
    dis = dis_x + dis_y
    if dis == step:
        return True
    elif dis < step and (step - dis) % 2 == 0:
        return True
    else:
        return False


current = [0, 0, 0]
c = 0
for i in range(N):
    if check(current, schedules[i]) == False:
        c = 1
        break
    current = schedules[i]

if c == 0:
    print("Yes")
else:
    print("No")


# ================================================================================= #

# N = int(input())
# times = []
# coordinates = {}

# for i in range(N):
#     coordinates["coordinates_{}".format(i)] = list(map(int, input().split()))

# # for key, value in coordinates.items():
# #     print(f"{key}: {value}")

# for key, value in coordinates.items():
#     times["times_{}".format(key)] = value.pop(0)
#     times = times.append(value)

#     # print(times)


# def cal_coodinates():
#     for key, value in coordinates.items():
#         value = "coordinates_{}".format(key)
#         print("\ntime: {}\nvalue: {}".format(times, value))
#         for i in range(times[i]):
#             test = []
#             for j in range(times[j]):
#                 test = []
#                 test.append(i)
#                 test.append(j)
#                 # print(test)
#                 if test == value:
#                     print("Yes")
#                     return test

#     print("NO")
#     exit()


# while N != 0:
#     cal_coodinates()
#     N -= 1

# 2
# 3 4 6
# 2 4 6
# coordinates_0: [3, 4, 6]
# coordinates_1: [2, 4, 6]
# {'times_coordinates_0': 3}
# {'times_coordinates_0': 3, 'times_coordinates_1': 2}

# N = int(input())

# count = 0
# prev_x = 0
# prev_y = 0
# prev_found = True


# def cal_coord(time, coordinates, count, prev_x, prev_y):
#     for i in range(time):
#         test = []
#         if count != 0:
#             test.append(prev_x)
#             test.append(prev_y)
#         for j in range(time):
#             test = []
#             test.append(i)
#             test.append(j)
#             print(test)
#             if test == coordinates:
#                 prev_x = i
#                 prev_y = j
#                 count += 1
#                 return True, count, prev_x, prev_y
#     count += 1
#     return False, count, prev_x, prev_y


# for _ in range(N):
#     coordinates = list(map(int, input().split()))
#     time = coordinates.pop(0)
#     # print("\nN: {}\nTime: {}\nCoordinates: {}".format(N, time, coordinates))

#     found, count, prev_x, prev_y = cal_coord(time, coordinates, count, prev_x, prev_y)
#     if found and count == N and prev_found != False:
#         print("YES")
#     elif count == N:
#         print("NO")
#     # else:
#     #     print("NO")

#     prev_found = found


# 2
# 3 1 2

# N: 2
# Time: 3
# Coordinates: [1, 2]
# Yes
