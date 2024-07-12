N = int(input())
ans = []
ans.append("L")
for _ in range(N):
    ans.append("o")
ans.append("ng")
print("".join(ans))

# Other Solution
N = int(input())

print("L", end="")
for i in range(N):
    print("o",
          end="")  # By default Python‘s print() function ends with a newline. A programmer with C/C++ background may wonder how to print without a newline. Python’s print() function comes with a parameter called ‘end‘. By default, the value of this parameter is ‘\n’, i.e. the new line character.
print("ng")
