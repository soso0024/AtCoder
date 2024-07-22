K, G, M = map(int, input().split())

g_ml, m_ml = 0, 0

for _ in range(K):
    if g_ml == G:
        g_ml = 0
        # print("Im there 1")
    elif m_ml == 0:
        m_ml = M
        # print("Im there 2")
    else:
        if m_ml > G:
            m_ml = m_ml - G + g_ml
            g_ml = G
            # print("Im there 3")
        else:
            g_ml = m_ml
            m_ml = 0
            # print("Im there 4")
print(g_ml, m_ml)
# print()

# Other Solution
k, g, m = map(int, input().split())
x, y = 0, 0

for i in range(k):
    if x == g:
        x = 0
    elif y == 0:
        y = m
    else:
        z = min(y, g - x)
        x, y = x + z, y - z

print(str(x) + " " + str(y))
