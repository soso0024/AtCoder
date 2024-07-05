S = input()

prefix = "ABC"
data = []
for i in range(1, 350):
    if i == 316:
        continue
    data.append(f"{prefix}{i:03d}")

for i in range(len(data)):
    if S == data[i]:
        print("Yes")
        exit()
print("No")


# Other Solution 1
S = input()
N = int(S[3:6])
if N == 316 or N == 000:
    print("No")
elif N <= 349:
    print("Yes")
else:
    print("No")

# 2
s = input()
num = int(s[3:6])
print("Yes" if 1 <= num <= 349 and num != 316 else "No")
