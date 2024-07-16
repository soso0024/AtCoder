S = input()

positions_a, positions_b, positions_c = [], [], []
if "A" in S:
    current_a = S.index("A")

    while True:
        idx_a = S.find("A", current_a)
        if idx_a == -1:
            break
        positions_a.append(idx_a)
        current_a = idx_a + 1
if "B" in S:
    current_b = S.index("B")
    while True:
        idx_b = S.find("B", current_b)
        if idx_b == -1:
            break
        positions_b.append(idx_b)
        current_b = idx_b + 1

if "C" in S:
    current_c = S.index("C")
    while True:
        idx_c = S.find("C", current_c)
        if idx_c == -1:
            break
        positions_c.append(idx_c)
        current_c = idx_c + 1

# print(positions_a, positions_b, positions_c)

if (
    (positions_a == [] and positions_b == [])
    or (positions_a == [] and positions_c == [])
    or (positions_b == [] and positions_c == [])
):
    print("Yes")
    exit()

if positions_a == []:
    if positions_b[-1] + 1 == positions_c[0]:
        print("Yes")
        exit()

if positions_b == []:
    if positions_a[-1] + 1 == positions_c[0]:
        print("Yes")
        exit()

if positions_c == []:
    if positions_a[-1] + 1 == positions_b[0]:
        print("Yes")
        exit()

if positions_a[-1] + 1 == positions_b[0] and positions_b[-1] + 1 == positions_c[0]:
    print("Yes")
else:
    print("No")
"""
A
[0] [] []

AAABBBCCCCCCC
[0, 1, 2] [3, 4, 5] [6, 7, 8, 9, 10, 11, 12]
"""

# Other Solution
s = list(input())
ans = "Yes"
for i in range(len(s) - 1):
    if s[i] == "B" and s[i + 1] == "A":
        ans = "No"
    if s[i] == "C" and (s[i + 1] == "A" or s[i + 1] == "B"):
        ans = "No"

print(ans)
