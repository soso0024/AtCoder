x, y = map(int, input().split())

if 0 <= (y - x) <= 2 or 0 >= y - x >= -3:
    print("Yes")
else:
    print("No")
