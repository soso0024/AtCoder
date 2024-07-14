N = int(input())
D = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for d in range(1, D[i] + 1):
        num = str(i + 1) + str(d)
        print(num)

        print(set(str(num)))
        if len(set(str(num))) == 1:
            cnt += 1

print(cnt)

"""
Example
Input: N = 2, D_1 = 3, D_2 = 5
Output:
2
3 5

11
{'1'}
12
{'1', '2'}
13
{'1', '3'}
21
{'1', '2'}
22
{'2'}
23
{'3', '2'}
24
{'4', '2'}
25
{'5', '2'}

cnt: 2


"""
