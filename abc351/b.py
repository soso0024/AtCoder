N = int(input())

A = []
B = []
ans_box_a = []
ans_box_b = []
result = []

for _ in range(N):
    a = list(map(str, input().split()))
    A.append(a)

for _ in range(N):
    b = list(map(str, input().split()))
    B.append(b)

# print("% ################## %")

for i in range(N):
    if A[i] != B[i]:
        ans_box_a += A[i]
        ans_box_b += B[i]
        result.append(i + 1)
        break

new_ans_box_a = list(ans_box_a[0])
new_ans_box_b = list(ans_box_b[0])

for i in range(N):
    if new_ans_box_a[i] != new_ans_box_b[i]:
        result.append(i + 1)
        break

print(" ".join(map(str, result)))

# print(list(ans_box_a))
# print(list(ans_box_a[0]))
# ['def']
# ['d', 'e', 'f']

# 3
# abc
# def
# ghi
# abc
# bef
# ghi
# % ################## %
# ['def']

# print(B[0])
# print(B[0][0])
# 3
# abc
# def
# ghi
# abc
# bef
# ghi
# % ################## %
# ['abc']
# abc
