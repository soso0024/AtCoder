R = int(input())

ans = 0
if R <= 99:
    ans = 100 - R
elif 100 <= R <= 199:
    ans = 200 - R
elif 200 <= R <= 299:
    ans = 300 - R
else:
    ans = 400 - R
print(ans)

# Other Solution
R = int(input())
print(100 - (R % 100))
