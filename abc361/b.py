a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())


def check(a, b, c, d):
    if d <= a or b <= c:
        return False
    return True


if check(a, d, g, j) and check(b, e, h, k) and check(c, f, i, l):
    print("Yes")
else:
    print("No")


# x = 0
# y = 0
# z = 0
# if a <= g:
#     if d <= j:
#         x = d - g
#     elif j < d:
#         x = j - g
#     else:
#         x = 0
#         # print("No")
#         print("No 1")
#         exit()

# if b <= h:
#     if e <= k:
#         y = e - h
#     elif k < e:
#         y = k - h
#     else:
#         y = 0
#         # print("No")
#         print("No 2")
#         exit()

# if c <= l:
#     if f <= l:
#         z = f - i
#     elif l < f:
#         z = l - i
#     else:
#         z = 0
#         # print("No")
#         print("No 3")
#         exit()

# # print(x, y, z)
# taiseki = x * y * z
# # print(taiseki)

# if x > 0 and y > 0 and z > 0:
#     if taiseki > 0:
#         print("Yes")
# else:
#     print("No")
