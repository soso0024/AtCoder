N = list(input())

a = int(N[0])
b = int(N[1])
c = int(N[2])

tol_N = a * 100 + b * 10 + c

if a * b == c:
    print("".join(N))
    print("Im here 1")
else:
    c = a * b
    if a * 100 + b * 10 + c > tol_N and c < 10:
        print(a * 100 + b * 10 + c)
        print("Im here 2")

    elif a * 100 + b * 10 + c < tol_N and a * (b + 1) < 10:
        b += 1
        c = a * b
        print(a * 100 + b * 10 + c)
        print("Im here 3")

    else:
        a += 1
        b = 0
        c = 0
        print(a * 100)
        print("Im here 4")

"""
413
414
Im here 2

214
300
Im here 3
"""

# Other Solution
n = int(input())

ans = 0
for i in range(n, 920):
    stri = str(i)
    if int(stri[0]) * int(stri[1]) == int(stri[2]):
        print(i)
        exit()
