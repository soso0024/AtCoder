from collections import deque

# 入力を受け取る
h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

# スタートとゴールの位置を見つける
for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            start = (i, j)
        if c[i][j] == "g":
            goal = (i, j)

# スタックを使って深さ優先探索を実行
waiting = deque()
waiting.append(start)
# 訪問済みを追跡するリスト
visited = [[0] * w for _ in range(h)]
visited[start[0]][start[1]] = 1

# 上下左右の移動を定義
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

found = False

while waiting:
    cur_pos = waiting.pop()
    # ゴールに到達した場合
    if cur_pos == goal:
        found = True
        break
    # 可能な方向に移動
    for direction in directions:
        next_pos = (cur_pos[0] + direction[0], cur_pos[1] + direction[1])
        # グリッド内に収まっているか確認
        if 0 <= next_pos[0] < h and 0 <= next_pos[1] < w:
            # 次の位置が通行可能で、まだ訪問していない場合
            if (c[next_pos[0]][next_pos[1]] == '.' or c[next_pos[0]][
                next_pos[1]] == 'g') and not visited[next_pos[0]][next_pos[1]]:
                waiting.append(next_pos)
                visited[next_pos[0]][next_pos[1]] = 1

# 結果を出力
if found:
    print("Yes")
else:
    print("No")
