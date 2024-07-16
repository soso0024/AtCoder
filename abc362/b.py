coordinates = []
for _ in range(3):
    coordinate = list(map(int, input().split()))
    coordinates.append(coordinate)
# print(coordinates)


def sq(x1, x2, y1, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


a = sq(coordinates[0][0], coordinates[1][0], coordinates[0][1], coordinates[1][1])
b = sq(coordinates[0][0], coordinates[2][0], coordinates[0][1], coordinates[2][1])
c = sq(coordinates[1][0], coordinates[2][0], coordinates[1][1], coordinates[2][1])

# a = (coordinates[1][0] - coordinates[0][0]) ** 2 + (
#     coordinates[1][1] - coordinates[0][1]
# ) ** 2
# print(a)
# b = (coordinates[2][0] - coordinates[0][0]) ** 2 + (
#     coordinates[2][1] - coordinates[0][1]
# ) ** 2
# print(b)
# c = (coordinates[2][0] - coordinates[1][0]) ** 2 + (
#     coordinates[2][1] - coordinates[1][1]
# ) ** 2
# print(c)

if a == (b + c) or b == (a + c) or c == (a + b):
    print("Yes")
    exit()

print("No")
