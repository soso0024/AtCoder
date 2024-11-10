m = int(input())

ans = []
a_i = 10
count = 0
while m > 0 and a_i >= 0:
    if m - 3**a_i < 0:
        a_i -= 1
    else:
        m -= 3**a_i
        ans.append(str(a_i))
        count += 1

print(count)
print(" ".join(ans))
