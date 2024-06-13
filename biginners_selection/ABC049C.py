S = input()
T_candidates = ["eraser", "erase", "dreamer", "dream"]

# print(type(S))

for i in T_candidates:
    # print(S)
    S = S.replace(i, "")

if len(S) == 0:
    print("YES")
else:
    print("NO")

# print(len(S))

# S = input()
# T = []
# T_candidates = ["", "dream", "dreamer", "erase", "eraser"]

# # print("S: {}\nT: ".format(S, T))

# for i in T_candidates:
#     for j in T_candidates:
#         for k in T_candidates:
#             for l in T_candidates:
#                 if i + j + k + l == S:
#                     print("YES")
#                     exit()

# print("NO")
