n, a, b = map(int, input().split())
total_sum = 0

for i in range(1, n + 1):
    if a <= sum(map(int, str(i))) <= b:
        total_sum += i

print(total_sum)

# for check
# for i in range(1, 15):
#     digit_sum = sum(map(int, str(i)))
#     print(f"{i} の桁の和は {digit_sum} です")

# 1 の桁の和は 1 です
# 2 の桁の和は 2 です
# 3 の桁の和は 3 です
# 4 の桁の和は 4 です
# 5 の桁の和は 5 です
# 6 の桁の和は 6 です
# 7 の桁の和は 7 です
# 8 の桁の和は 8 です
# 9 の桁の和は 9 です
# 10 の桁の和は 1 です
# 11 の桁の和は 2 です
# 12 の桁の和は 3 です
# 13 の桁の和は 4 です
# 14 の桁の和は 5 です


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
