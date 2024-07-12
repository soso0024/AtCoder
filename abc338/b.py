from collections import Counter

S = list(input())
S_alphabet = sorted(S)
# print(S)
cnt = Counter(S_alphabet)
# print(cnt)
print(max(cnt, key=cnt.get))
