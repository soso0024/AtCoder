N = int(input())

if N < 3:
    print("N >= 3")
    exit()

S = input()

if N != len(S):
    print("NOOOO")
    exit()

count = 0
pos_first_one = 0
pos_second_one = 0
pos_star = 0

for i in range(N):
    if S[i] == "|" and count == 0:
        pos_first_one = i
        count += 1
    elif S[i] == "|" and count == 1:
        pos_second_one = i

    if S[i] == "*":
        pos_star = i

    # print(pos_first_one, pos_second_one, pos_star)

    if pos_first_one < pos_star < pos_second_one:
        print("in")
        exit()

print("out")

# print("\nN: {}\nS: {}".format(N, S))
