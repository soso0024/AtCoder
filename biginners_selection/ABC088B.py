N = int(input())  # int!!!
A = list(map(int, input().split()))  # map(function, iterable, ...)

if N != len(A):
    print(len(A))
    print("Exit!")
    exit()

sorted_A = sorted(A)
# print(sorted_A)
# print(len(sorted_A))

Alice_point = 0
Bob_point = 0

# print(sorted_A.pop())

while len(sorted_A) != 0:
    Alice_point += sorted_A.pop()
    if len(sorted_A) != 0:
        Bob_point += sorted_A.pop()
    else:
        break

dif_point = Alice_point - Bob_point
print(dif_point)
