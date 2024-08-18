X = list(input())

while X[-1] == "0" or X[-1] == ".":
    if X.pop() == ".":
        break

print("".join(X))
