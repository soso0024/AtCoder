r, g, b = map(int, input().split())
c = input()

if c == "Red":
    if g > b:
        print(b)
    else:
        print(g)
elif c == "Blue":
    if r > g:
        print(g)
    else:
        print(r)
else:
    if r > b:
        print(b)
    else:
        print(r)

# Other Solution
R, G, B = map(int, input().split())
C = input()

if C == "Red":
    print(min(G, B))
elif C == "Green":
    print(min(R, B))
else:
    print(min(R, G))
