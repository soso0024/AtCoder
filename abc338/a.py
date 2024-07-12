S = input()

if S[0].isupper():
    for i in range(1, len(S)):
        if S[i].isupper():
            print("No")
            exit()
else:
    print("No")
    exit()

print("Yes")

# Other Solution
S = input()

if S == S.capitalize():  # The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
    print('Yes')
else:
    print('No')
