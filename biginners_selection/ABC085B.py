N = int(input())  # int!!!
A = []
while True:
    line = input()
    A.append(int(line))
    if N == len(A):
        break
# print(A)

# print("\n{}".format(A))
A_sorted = sorted(A)

A_unique = set(A_sorted)

# print(A_unique)
# [2, 5, 1]
# {1, 2, 5}

print(len(A_unique))
# print(A_unique)

# Other Solution
# n=int(input())
# ds=[]
# for i in range(n):
#     d=int(input())
#     ds.append(d)
# print(len(set(ds)))
