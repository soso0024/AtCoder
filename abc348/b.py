import math

N = int(input())


def cal_distance(x1, x2, y1, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


coordinates = []
for i in range(N):
    inp = list(map(int, input().split()))
    coordinates.append(inp)
# print(coordinates)
# [[0, 0], [2, 4], [5, 0], [3, 4]]
# print(
#     cal_distance(
#         coordinates[0][0], coordinates[1][0], coordinates[0][1], coordinates[1][1]
#     )
# )


j = 0
while j < N:
    ans_candi = 0
    biggest = 0
    for i in range(N):
        val = cal_distance(
            coordinates[j][0],
            coordinates[i][0],
            coordinates[j][1],
            coordinates[i][1],
        )

        if val > biggest:
            ans_candi = i + 1  # index starts from 0
            biggest = val
            # print(f"{val}, {biggest}")

    print(ans_candi)
    j += 1
