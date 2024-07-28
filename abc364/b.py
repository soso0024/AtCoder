H, W = map(int, input().split())
s_i, s_j = map(int, input().split())

C = []
for _ in range(H):
    c = list(input())
    C.append(c)
X = input()
# print(C)
# [['.', '#', '.'],
#  ['.', '.', '.']]

# print(len(X))
for i in range(len(X)):
    if X[i] == "U" and s_i - 1 > 0 and C[s_i - 1 - 1][s_j - 1] != "#":
        s_i -= 1

    if X[i] == "D" and s_i + 1 <= H and C[s_i - 1 + 1][s_j - 1] != "#":
        s_i += 1

    if X[i] == "R" and s_j + 1 <= W and C[s_i - 1][s_j - 1 + 1] != "#":
        s_j += 1

    if X[i] == "L" and s_j - 1 > 0 and C[s_i - 1][s_j - 1 - 1] != "#":
        s_j -= 1

print(f"{s_i} {s_j}")
