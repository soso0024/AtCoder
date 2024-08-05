N = int(input())
A = list(map(int, input().split()))
# print(A)

sorted_A = sorted(A, reverse=True)
# print(sorted_A)

best_two = sorted_A[1]
# print(best_two)

idx = A.index(best_two)
print(idx + 1)
