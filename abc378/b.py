# 1. 入力を受け取る
N = int(input())  # ゴミの種類数
q = [0] * N  # 各ゴミの収集間隔
r = [0] * N  # 各ゴミの最初の収集日

# 2. 各ゴミの収集スケジュールを受け取る
for i in range(N):
    q[i], r[i] = map(int, input().split())

# 3. 質問の数を受け取る
Q = int(input())

# 4. 各質問に答える
for _ in range(Q):
    # ゴミの種類と出す日を受け取る
    t, d = map(int, input().split())
    t -= 1  # 0から始まるインデックスに調整

    # dをqで割った商と余りを計算
    b, c = divmod(d, q[t])

    # 余り(c)と最初の収集日(r)を比較
    if c <= r[t]:
        a = b  # その周の収集日
    else:
        a = b + 1  # 次の周の収集日
    ans = a * q[t] + r[t]

    # 答えを出力
    print(ans)
