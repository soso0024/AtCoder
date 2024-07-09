from collections import Counter

w, b = map(int, input().split())
l = w + b

s = "wbwbwwbwbwbw"
while len(s) < l + 12:
    s += "wbwbwwbwbwbw"

# while l >= 13:
#     s += "wbwbwwbwbwbw"
#     print(s)
#     l -= 12
# print(s)

for i in range(len(s) - l + 1):
    counts = Counter(s[i:l + i])
    print(counts)
    if counts['w'] == w and counts['b'] == b:
        print("Yes")
        exit()
print("No")

# Other Solution
w, b = map(int, input().split())

a = 'wbwbwwbwbwbw'

for i in range(len(a) + 1):
    tmp = ''
    for j in range(200):
        tmp += a[(i + j) % 12]
        if tmp.count('w') == w and tmp.count('b') == b:
            print('Yes')
            exit()
print('No')
