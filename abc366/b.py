N = int(input())
S = []
max_length = -1
for _ in range(N):
    s = input()
    S.append(s)
    max_length = max(max_length, len(s))
# print(S)
# ['abc', 'de', 'fghi']
# print(max_length)

S = [s.ljust(max_length) for s in S]
# print(S)
print()

for j in range(max_length):
    output = []
    last_character = []
    for i in range(N - 1, -1, -1):
        if S[i][j] == " " and i == 0:
            break

        if S[i][j] == " ":
            output.append("*")
            last_character = "*"
        else:
            output.append(S[i][j])
            last_character = S[i][j]

    while output[-1] == "*":  # つまずきポイント
        output.pop()
    print("".join(output))
    # print(f"last character: {last_character}")
