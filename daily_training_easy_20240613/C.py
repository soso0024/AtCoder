N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if len(A) != N or len(B) != N:
    print("Invalid!!!")
    exit()

point_one = 0
point_two = 0

for i in range(N):
    for j in range(N):
        if A[i] == B[j] and i == j:
            point_one += 1
        elif A[i] == B[j] and i != j:
            point_two += 1

print(point_one)
print(point_two)
