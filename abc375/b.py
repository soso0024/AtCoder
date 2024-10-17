import math

N = int(input())
coordinates = [list(map(int, input().split())) for _ in range(N)]

dis_cost = 0

dis_cost += math.sqrt(coordinates[0][0] ** 2 + coordinates[0][1] ** 2)

for i in range(N - 1):
    dx = coordinates[i][0] - coordinates[i + 1][0]
    dy = coordinates[i][1] - coordinates[i + 1][1]
    distance = math.sqrt(dx**2 + dy**2)
    dis_cost += distance

dis_cost += math.sqrt(coordinates[-1][0] ** 2 + coordinates[-1][1] ** 2)

print(dis_cost)
