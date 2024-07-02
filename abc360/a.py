S = input()

if len(S) != 3:
    print("error")
    exit()

rice_idx = 0
miso_idx = 0

for i in range(len(S)):
    if S[i] == "R":
        rice_idx = i
    elif S[i] == "M":
        miso_idx = i

if rice_idx < miso_idx:
    print("Yes")
else:
    print("No")
