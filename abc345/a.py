S = input()

first = S[0]
last = S[-1]

if first == "<" and last == ">":
    for i in range(1, len(S) - 1):
        if S[i] == "=":
            continue
        else:
            print("No")
            exit()
    print("Yes")
else:
    print("No")
    exit()

# Other Solution
s = list(input())
if s[0] == "<" and s[-1] == ">":
    if s.count("=") == len(s) - 2:
        print("Yes")
        exit()
print("No")
