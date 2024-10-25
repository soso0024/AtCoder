def num_move(n, from_, to, ng):
    if from_ > to:
        from_, to = to, from_  # always from_ <= to

    if from_ <= ng <= to:
        return from_ + n - to  # (from_ - 1) + 1 + (N - to)
    else:
        return to - from_


n, q = map(int, input().split())
l, r = 1, 2
ans = 0
for _ in range(q):
    h, t = input().split()
    t = int(t)
    if h == "L":
        ans += num_move(n, l, t, r)
        l = t
    else:
        ans += num_move(n, r, t, l)
        r = t
print(ans)
