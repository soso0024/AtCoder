n = int(input())
s = input()

if n != len(s):
    print("Exit")
    exit()

for i in range(n - 1):
    if (s[i] == "a" and s[i + 1] == "b") or (s[i] == "b" and s[i + 1] == "a"):
        print("Yes")
        exit()

print("No")

# Other Solution
N = int(input())
S = input()
if S.find("ab") >= 0 or S.find("ba") >= 0:
    print("Yes")
else:
    print("No")
