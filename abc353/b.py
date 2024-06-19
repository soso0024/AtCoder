N, M = map(int, input().split())
A = list(map(int, input().split()))

if N != len(A):
    print("Exit")
    exit()

num_action = 0
remain_seats = M

for i in range(N):
    if remain_seats - A[i] < 0:
        num_action += 1
        # print(f"Count! i = {i}")
        remain_seats = M - A[i]
    else:
        remain_seats -= A[i]

print(num_action + 1)

# 7 6
# 2 5 1 4 1 2 3
# Count! i = 1
# Count! i = 5
# 2
