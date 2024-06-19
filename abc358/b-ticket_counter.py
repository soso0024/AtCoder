N, A = map(str, input().split())
t_list = input().split()
T_list = [int(num) for num in t_list]

waiting = 0
time = 0

for i in range(int(N)):
    time = (T_list[i]) + int(A) + waiting

    if i < int(N) - 1:
        waiting = time - T_list[i + 1]
    else:
        waiting = 0

    if waiting < 0:
        waiting = 0

    # print("time = {} + {}".format(T_list[i], int(A)))
    print(time)
