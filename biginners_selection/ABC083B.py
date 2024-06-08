n, a, b = map(int, input().split())
total_sum = 0

for i in range(1, n + 1):
    if a <= sum(map(int, str(i))) <= b:
        total_sum += i

print(total_sum)


# if 1 <= a <= b <= 36 or 1 <= n <= 10**4:
#     for i in range(1, n + 1):
#         temp = 0
#         if a <= i <= b and 1 <= i <= 9:
#             sum += i
#             print(i)
#             continue

#         if i >= 10:
#             temp = i % 10
#             if 10 <= i <= 19:
#                 temp += 1
#             if 20 <= i <= 29:
#                 temp += 2
#             if 30 <= i <= 36:
#                 temp += 3

#         if a <= temp <= b:
#             print(i)
#             sum += i

#     print(sum)
#     # print("\nsum: {}".format(sum))

# else:
#     print("error")
