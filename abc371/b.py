n, m = map(int, input().split())
taro_exist = [False for i in range(n)]
# print(taro_exist)
# 2 4
# [False, False]

for i in range(m):
    a, b = map(str, input().split())
    a = int(a) - 1
    if taro_exist[a] or b == "F":
        print("No")
    else:
        print("Yes")
        taro_exist[a] = True
