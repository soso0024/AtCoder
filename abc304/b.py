N = int(input())
ans = ""
if 10**3 - 1 >= N:
    ans = N
elif 10**4 - 1 >= N:
    ans = str(N // 10)
    ans += "0"
elif 10**5 - 1 >= N:
    ans += str(N // 100)
    ans += "00"
elif 10**6 - 1 >= N:
    ans = str(N // 1000)
    ans += "000"
elif 10**7 - 1 >= N:
    ans = str(N // 10000)
    ans += "0000"
elif 10**8 - 1 >= N:
    ans = str(N // 100000)
    ans += "00000"
elif 10**9 - 1 >= N:
    ans = str(N // 1000000)
    ans += "000000"
print(ans)

# Another Solution
n = [*input()]  # same as list(input())

for i in range(3, len(n)):
    n[i] = "0"

print("".join(n))
