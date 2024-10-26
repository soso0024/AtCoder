from copy import deepcopy

N = int(input())
A = []
for _ in range(N):
    row = list(input().strip())
    A.append(row)

for i in range(1, N // 2 + 1):
    # 一時的な配列を作成
    B = deepcopy(A)

    # i以上N+1-i以下の範囲で処理
    for x in range(i - 1, N - i + 1):
        for y in range(i - 1, N - i + 1):
            # (x,y)の色を(y,N-1-x)に移動
            B[y][N - 1 - x] = A[x][y]

    # 一括更新
    A = B

print()
# 結果の出力
for row in A:
    print(*row, sep="")
