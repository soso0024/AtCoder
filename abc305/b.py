p, q = map(str, input().split())

if p == "A":
    p = 0
elif p == "B":
    p = 3
elif p == "C":
    p = 4
elif p == "D":
    p = 8
elif p == "E":
    p = 9
elif p == "F":
    p = 14
elif p == "G":
    p = 23

if q == "A":
    q = 0
elif q == "B":
    q = 3
elif q == "C":
    q = 4
elif q == "D":
    q = 8
elif q == "E":
    q = 9
elif q == "F":
    q = 14
elif q == "G":
    q = 23

print(abs(p - q))

# Other Solution
p, q = input().split()

B_dic = {"A": 0, "B": 3, "C": 4, "D": 8, "E": 9, "F": 14, "G": 23}

print(abs(B_dic[p] - B_dic[q]))
