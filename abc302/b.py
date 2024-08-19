H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())
# print(S)

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

T = "snuke"

for si in range(H):
    for sj in range(W):
        for v in range(8):
            i = si
            j = sj
            for k in range(5):
                if i < 0 or j < 0 or i >= H or j >= W:
                    break
                if S[i][j] != T[k]:
                    break
                if k == 4:
                    i = si
                    j = sj
                    for nk in range(5):
                        print(f"{i+1} {j+1}")
                        i += di[v]
                        j += dj[v]
                i += di[v]
                j += dj[v]
