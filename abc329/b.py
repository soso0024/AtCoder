N = int(input())
A = list(map(int, input().split()))

set_a = list(set(A))
sorted_A = sorted(set_a)
# print(set_a)
# print(sorted_A)
print(sorted_A[len(sorted_A) - 2])
