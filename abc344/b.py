A = []
while True:
    num = int(input())
    if num == 0:
        A.append(num)
        break
    A.append(num)

# print(A)

ans = []
i = len(A) - 1
while i >= 0:
    ans.append(str(A[i]))
    i -= 1

# print(ans)
# ['1', '2']
print("\n".join(ans))
