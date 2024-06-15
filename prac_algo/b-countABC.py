N = int(input())
S = input()

if N != len(S):
    print("Nooooo")
    exit()

# count = 0
tol_count = 0

for i in range(N - 2):
    if S[i] == "A" and S[i + 1] == "B" and S[i + 2] == "C":
        tol_count += 1

# for i in range(N):
#     if count == 0:
#         if S[i] == "A":
#             # print(i)
#             count += 1
#             continue
#         else:
#             count = 0

#     # if count == 1 and S[i] == "B":
#     #     print(i)
#     #     count += 1

#     if count == 1:
#         if S[i] == "B":
#             # print(i)
#             count += 1
#             continue
#         else:
#             # print("Here !")
#             count = 0

#     if count == 2:
#         if S[i] == "C":
#             # print(i)
#             tol_count += 1
#             # print("Count One !\n")
#         count = 0


print(tol_count)
