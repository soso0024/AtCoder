N, M = map(int, input().split())
S = input()  # N is Length of S
T = input()  # M is Length of T

# first = T[0] + T[1] + T[2]
# print(first)
# back = T[-3] + T[-2] + T[-1]
# print(back)

first = ""
for i in range(N):
    first += T[i]
back = ""
for i in range(N, 0, -1):
    back += T[-i]

print(first)
print(back)

if S == first and S == back:
    print(0)
elif S == first and S != back:
    print(1)
elif S != first and S == back:
    print(2)
else:
    print(3)
