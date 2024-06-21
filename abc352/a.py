N, X, Y, Z = list(map(int, input().split()))

start_pos = X
goal_pos = Y

while start_pos != goal_pos:
    if start_pos > goal_pos:
        start_pos -= 1
    elif start_pos < goal_pos:
        start_pos += 1

    if start_pos == Z:
        print("Yes")
        exit()

print("No")
