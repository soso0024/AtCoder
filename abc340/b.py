Q = int(input())
que = []
for _ in range(Q):
    a, b = map(int, input().split())
    if a == 1:
        que.append(b)
    if a == 2:
        print(que[len(que) - b])
