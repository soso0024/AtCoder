S, T = input().split()

len_S = len(S)

for w in range(len_S):
    for c in range(w):
        ss = ""
        for k in range(0, len_S, w):
            try:
                ss += S[k + c]
                print(f"ss={ss} k={k} c={c}")
            except:
                print("Im here")
                pass
        if ss == T:
            print("Yes")
            exit()

print("No")
