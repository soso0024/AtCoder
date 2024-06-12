n, y = map(int, input().split())

num_ichiman = 0
num_gosen = 0
num_senen = 0

for i in range(n + 1):
    for j in range(n + 1 - i):
        k = n - i - j
        if (10000 * i + 5000 * j + 1000 * k) == y:
            num_ichiman = i
            num_gosen = j
            num_senen = k
            # print(i, j, k)
            break
    if (num_ichiman + num_gosen + num_senen) == n:
        print(num_ichiman, num_gosen, num_senen)
        exit()

print(-1, -1, -1)


# for i in range(1, 2000):
#     if y >= 10000:
#         y -= 10000
#         print(y)
#         num_ichiman += 1
#         tol_n += 1
#     else:
#         break

# for i in range(1, 2000):
#     if y > 5000:
#         y -= 5000
#         num_gosen += 1
#         tol_n += 1
#     else:
#         break

# for i in range(1, 2000):
#     if y >= 1000:
#         y -= 1000
#         num_senen += 1
#         tol_n += 1
#     else:
#         break

# print(num_ichiman, num_gosen, num_senen, tol_n)
